
from Page.OrderConfirmationPage import OrderConfirmationPage
import pytest
import allure
from pathlib import Path
from playwright.sync_api import sync_playwright,expect
@pytest.mark.regression
class Test_checkOutComplete:

   def test_current_url(self, orderconfirmation):
        with allure.step("Verify order confirmation URL"):
            assert "https://www.saucedemo.com/checkout-complete.html" in orderconfirmation.get_current_url()

def test_dashboard_text(self, orderconfirmation):
    with allure.step("Verify confirmation dashboard"):
        assert "Swag Labs" in orderconfirmation.get_dashboard_text()

def test_verify_order_status(self, orderconfirmation):
    with allure.step("Verify order status"):
        assert orderconfirmation.get_order_status() == "Checkout: Complete!"

def test_verify_success_message(self, orderconfirmation):
    with allure.step("Verify success message"):
        assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" in orderconfirmation.get_success_message()

def test_download_pdf_order(self, orderconfirmation, tmp_path: Path):
    with allure.step("Download order PDF"):
        file_path = Path(orderconfirmation.download_pdf_order(target_dir=str(tmp_path)))
        assert file_path.exists(), "Downloaded file does not exist"
        assert file_path.stat().st_size > 0, "Downloaded file is empty"

def test_click_hamburger_menu(self, orderconfirmation):
    with allure.step("Open hamburger menu"):
        orderconfirmation.hamburger.click()
        expect(orderconfirmation.logout).to_be_visible()

def test_logout(self, orderconfirmation):
    with allure.step("Log out"):
        if not orderconfirmation.logout.is_visible():
            orderconfirmation.hamburger.click()
        orderconfirmation.logout.click()
        assert "saucedemo.com" in orderconfirmation.get_current_url()