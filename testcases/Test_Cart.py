import pytest
import allure
from playwright.sync_api import sync_playwright,expect

@pytest.mark.regression
class Test_cart:

    def test_view_cart(self, cartpage):
        with allure.step("Open cart page"):
            cartpage.view_cart()
            assert 'https://www.saucedemo.com/cart.html' in cartpage.page.url

    def test_verify_quantity(self, cartpage):
        with allure.step("Verify cart quantity"):
            assert cartpage.get_quantity() == "1"

    def test_verify_item_name(self, cartpage):
        with allure.step("Verify cart item name"):
            assert cartpage.get_item_name() == "Sauce Labs Backpack"

    def test_verify_price(self, cartpage):
        with allure.step("Verify cart price"):
            assert cartpage.get_price() == "$29.99"

    def test_verify_remove_button_active(self, cartpage):
        with allure.step("Verify remove button"):
            expect(cartpage.remove_item()).to_be_visible()

    def test_checkout_button(self, cartpage):
        with allure.step("Verify checkout button"):
            expect(cartpage.get_checkout_button()).to_be_visible()

    def test_click_checkout_button(self, cartpage):
        with allure.step("Open checkout page"):
            expect(cartpage.get_checkout_button()).to_be_visible()
            cartpage.click_checkout_button()