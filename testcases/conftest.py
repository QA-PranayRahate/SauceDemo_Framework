
import os
import pytest
import allure
import json
import re
import sys
import shutil
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

# Add testcases directory to path so page objects can be imported
sys.path.insert(0, str(Path(__file__).parent))

from Page.HomePage import HomePage
from Page.CartPage import CartPage
from Page.checkoutPage import CheckoutPage
from Page.payementPage import PayementPage
from Page.LoginPage import LoginPage
from Page.ProductPage import ProductPage
from Page.OrderConfirmationPage import OrderConfirmationPage

with (Path(__file__).parent.parent / ".auth" / "login_details.json").open(encoding='utf-8') as login_details_file:
    LOGIN_DETAILS = json.load(login_details_file)

DEFAULT_USERNAME = LOGIN_DETAILS['username']
DEFAULT_PASSWORD = LOGIN_DETAILS['password']


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if not report.failed:
        return

    page = item.funcargs.get('page')
    if page is None:
        return

    screenshot_dir = Path('screenshots')
    screenshot_dir.mkdir(exist_ok=True)
    filename = re.sub(r'[^A-Za-z0-9_.-]+', '_', item.nodeid) + '.png'
    screenshot_path = screenshot_dir / filename

    try:
        screenshot = page.screenshot(path=str(screenshot_path), full_page=True)
        allure.attach(
            screenshot,
            name=f'{item.name} failure screenshot',
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception as error:
        terminal_reporter = item.config.pluginmanager.get_plugin('terminalreporter')
        if terminal_reporter:
            terminal_reporter.write_line(
                f'Unable to capture failure screenshot for {item.nodeid}: {error}'
            )


@pytest.fixture(scope="session")
def browser():
    headless = os.getenv("HEADLESS", "false").lower() == "true"   # added
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=headless,                      # was: headless=False
            args=["--start-maximized"],
        )
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def authenticated_state(browser):
    """Login once and save the storage state for reuse in other tests"""
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://www.saucedemo.com")
    
    # Perform login with credentials from JSON
    loginpage = LoginPage(page)
    loginpage.login_as_standard_user(DEFAULT_USERNAME, DEFAULT_PASSWORD)
    
    # Save the authenticated state
    context.storage_state(path="state.json")
    
    context.close()
    yield "state.json"

@pytest.fixture(scope="session")
def page(browser, authenticated_state):
    """Use authenticated session from saved state"""
    context = browser.new_context(
        no_viewport=True,
        storage_state=authenticated_state
    )
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")

    try:
        yield page
    finally:
        Path("traces").mkdir(exist_ok=True)
        context.tracing.stop(path="traces/trace.zip")
        context.close()


@pytest.fixture(scope='class')
def loginpage(page):
    return LoginPage(page)

@pytest.fixture(scope='class')
def homepage(page):
    # page.goto("https://www.saucedemo.com/inventory.html")
    return HomePage(page)

@pytest.fixture(scope='class')
def productpage(page):
    page.goto("https://www.saucedemo.com/inventory-item.html?id=4")
    return ProductPage(page)

@pytest.fixture(scope='class')
def cartpage(page):
    # page.goto("https://www.saucedemo.com/inventory.html")
    # ProductPage(page).add_product_to_cart()
    page.goto("https://www.saucedemo.com/cart.html")
    return CartPage(page)

@pytest.fixture(scope='class')
def checkoutpage(page):
    page.goto("https://www.saucedemo.com/checkout-step-one.html")
    return CheckoutPage(page)

@pytest.fixture(scope='class')
def paymentpage(page):
    page.goto("https://www.saucedemo.com/checkout-step-two.html")
    return PayementPage(page)

@pytest.fixture(scope='class')
def orderconfirmation(page):
    page.goto('https://www.saucedemo.com/checkout-complete.html')
    return OrderConfirmationPage(page)


def pytest_sessionfinish(session, exitstatus):
    allure_results_path = Path('allure-results').resolve()
    terminal_reporter = session.config.pluginmanager.get_plugin('terminalreporter')

    if terminal_reporter:
        terminal_reporter.write_sep('=', 'Test reports')
        terminal_reporter.write_line(f'Allure results: {allure_results_path}')
        terminal_reporter.write_line('Allure command: allure serve allure-results')

    allure_command = (
        shutil.which('allure.cmd')
        or shutil.which('allure.exe')
        or shutil.which('allure')
    )
    if allure_command and allure_results_path.exists():
        if allure_command.lower().endswith('.ps1'):
            command = [
                'powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass',
                '-File', allure_command, 'serve', str(allure_results_path),
            ]
        else:
            command = [allure_command, 'serve', str(allure_results_path)]

        try:
            subprocess.Popen(
                command,
                creationflags=getattr(subprocess, 'CREATE_NEW_PROCESS_GROUP', 0),
            )
        except OSError as error:
            if terminal_reporter:
                terminal_reporter.write_line(f'Unable to launch Allure: {error}')