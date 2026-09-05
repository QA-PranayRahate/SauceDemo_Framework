import pytest
import allure
from playwright.sync_api import sync_playwright,expect
@pytest.mark.regression
class Test_checkout:

    def test_current_url(self, checkoutpage):
        with allure.step("Verify checkout URL"):
            assert 'https://www.saucedemo.com/checkout-step-one.html' in checkoutpage.get_current_url()
    
    def test_enter_first_name(self, checkoutpage):
        with allure.step("Enter first name"):
            checkoutpage.enter_first_name("Alex")

    def test_enter_last_name(self, checkoutpage):
        with allure.step("Enter last name"):
            checkoutpage.enter_last_name("marvel")

    def test_enter_zip_code(self, checkoutpage):
        with allure.step("Enter postal code"):
            checkoutpage.enter_postal_code("19293")

    def test_click_continue_button(self, checkoutpage):
        with allure.step("Continue to payment"):
            expect(checkoutpage.continue_button).to_be_visible()
            checkoutpage.click_continue_button()