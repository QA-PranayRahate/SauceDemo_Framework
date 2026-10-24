
import os
import pytest
import allure
import re
import sys
import shutil
import subprocess
from pathlib import Path
from dotenv import load_dotenv
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

load_dotenv(Path(__file__).parent.parent / ".env")

def pytest_addoption(parser):
    parser.addoption(
        "--my-browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "webkit"],
        help="Browser to run tests on",
    )
    parser.addoption(
        "--no-headed",
        action="store_true",
        default=False,
        help="Run the browser in headless mode",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if not report.failed:
        return

    page = item.funcargs.get('page')
    if page is None or page.is_closed():
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
def browser(request):
    headless = (
        request.config.getoption("--no-headed")
        or os.getenv("HEADLESS", "false").lower() == "true"
    )
    browser_name = request.config.getoption("--my-browser")

    with sync_playwright() as playwright:
        if browser_name == "chrome":
            browser = playwright.chromium.launch(
                headless=headless,
                args=["--start-maximized"],
            )
        elif browser_name == "firefox":
            browser = playwright.firefox.launch(headless=headless,args=["--start-maximized"])
        elif browser_name == "webkit":
            browser = playwright.webkit.launch(headless=headless,args=["--start-maximized"])
        elif browser_name=='edge':
            browser=playwright.chromium.launch(channel='msedge',headless=headless,args=["--start-maximized"])
        else:
            raise pytest.UsageError(
                f"Unsupported browser '{browser_name}'. Choose chromium, firefox, or webkit."
            )

        yield browser
        browser.close()

@pytest.fixture(scope="session")
def page(browser):
    """Share one browser page across the ordered test flow."""
    context = browser.new_context(no_viewport=True)
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    page = context.new_page()
    page.goto("https://www.saucedemo.com")

    try:
        yield page
    finally:
        Path("traces").mkdir(exist_ok=True)
        context.tracing.stop(path="traces/trace.zip")
        context.close()

@pytest.fixture
def login_credentials():
    username = os.getenv("SWAG_DEMO_USERNAME")
    password = os.getenv("SWAG_DEMO_PASSWORD")
    if not username or not password:
        raise pytest.UsageError(
            "Set SWAG_DEMO_USERNAME and SWAG_DEMO_PASSWORD in the root .env file "
            "or in the environment."
        )
    return username, password


@pytest.fixture(scope='class')
def loginpage(page):
    return LoginPage(page)

@pytest.fixture(scope='class')
def homepage(page):
    # page.goto("https://www.saucedemo.com/inventory.html")
    return HomePage(page)

@pytest.fixture(scope='class')
def productpage(page):
    product_page = ProductPage(page)
    product_page.click_product_by_name()
    return product_page

@pytest.fixture(scope='class')
def cartpage(page):
    return CartPage(page)

@pytest.fixture(scope='class')
def checkoutpage(page):
    return CheckoutPage(page)

@pytest.fixture(scope='class')
def paymentpage(page):
    return PayementPage(page)

@pytest.fixture(scope='class')
def orderconfirmation(page):
    return OrderConfirmationPage(page)


def pytest_sessionfinish(session, exitstatus):
    allure_results_path = Path('allure-results').resolve()
    allure_report_path = Path('allure-report').resolve()
    terminal_reporter = session.config.pluginmanager.get_plugin('terminalreporter')

    allure_command = (
        shutil.which('allure.cmd')
        or shutil.which('allure.exe')
        or shutil.which('allure')
    )
    if not allure_results_path.exists():
        if terminal_reporter:
            terminal_reporter.write_line(
                f'Allure results directory does not exist: {allure_results_path}'
            )
        return

    if not allure_command:
        if terminal_reporter:
            terminal_reporter.write_line(
                'Allure CLI was not found; results were saved to '
                f'{allure_results_path}, but the HTML report was not generated.'
            )
        return

    if allure_command.lower().endswith('.ps1'):
        command = [
            'powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass',
            '-File', allure_command, 'generate', str(allure_results_path),
            '--clean', '-o', str(allure_report_path),
        ]
    else:
        command = [
            allure_command, 'generate', str(allure_results_path),
            '--clean', '-o', str(allure_report_path),
        ]

    result = subprocess.run(command, check=False)
    if terminal_reporter:
        if result.returncode == 0:
            terminal_reporter.write_line(
                f'Allure HTML report generated: {allure_report_path}'
            )
        else:
            terminal_reporter.write_line(
                f'Allure report generation failed with exit code {result.returncode}. '
                f'Results remain available at {allure_results_path}.'
            )