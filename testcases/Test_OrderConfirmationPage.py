
import pytest
import allure
from playwright.sync_api import expect

@pytest.mark.regression
@pytest.mark.run(order=7)
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

    def test_back_home_button(self, orderconfirmation):
        with allure.step("Verify Back Home button"):
            expect(orderconfirmation.back_home_button).to_be_visible()

    def test_click_hamburger_menu(self, orderconfirmation):
        with allure.step("Open hamburger menu"):
            orderconfirmation.hamburger.click()
            expect(orderconfirmation.logout_button).to_be_visible()

    def test_logout(self, orderconfirmation):
        with allure.step("Log out"):
            if not orderconfirmation.logout_button.is_visible():
                orderconfirmation.hamburger.click()
            orderconfirmation.logout_button.click()
            assert "saucedemo.com" in orderconfirmation.get_current_url()