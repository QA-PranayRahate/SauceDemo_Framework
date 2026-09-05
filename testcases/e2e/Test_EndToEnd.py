import pytest
import allure

from Page.CartPage import CartPage
from Page.HomePage import HomePage
from Page.ProductPage import ProductPage
from Page.checkoutPage import CheckoutPage
from Page.payementPage import PayementPage
from Page.OrderConfirmationPage import OrderConfirmationPage


@pytest.mark.regression
@allure.feature("Purchase flow")
@allure.story("Complete purchase")
@allure.severity(allure.severity_level.CRITICAL)
class TestEndToEnd:
    @allure.title("Complete purchase from inventory to order confirmation")
    @allure.description("Validates the complete authenticated SauceDemo purchase journey.")
    def test_complete_purchase_flow(self, page):
        with allure.step("Verify the inventory page"):
            home_page = HomePage(page)
            assert home_page.get_current_url().endswith("/inventory.html")
            assert home_page.get_dashboard_text() == "Swag Labs"

        with allure.step("Add the backpack to the cart"):
            product_page = ProductPage(page)
            assert product_page.get_product_name() == "Sauce Labs Backpack"
            assert "$29.99" in product_page.get_product_price()
            product_page.add_product_to_cart()
            assert product_page.is_product_added()

        with allure.step("Verify the cart and open checkout"):
            cart_page = CartPage(page)
            cart_page.view_cart()
            assert page.url.endswith("/cart.html")
            assert cart_page.get_quantity() == "1"
            assert cart_page.get_item_name() == "Sauce Labs Backpack"
            assert cart_page.get_price() == "$29.99"
            cart_page.click_checkout_button()

        with allure.step("Complete checkout details"):
            checkout_page = CheckoutPage(page)
            checkout_page.enter_first_name("Test")
            checkout_page.enter_last_name("User")
            checkout_page.enter_postal_code("12345")
            assert checkout_page.get_current_url().endswith("/checkout-step-one.html")
            checkout_page.click_continue_button()

        with allure.step("Verify payment summary and finish the order"):
            payment_page = PayementPage(page)
            assert payment_page.get_current_url().endswith("/checkout-step-two.html")
            assert payment_page.get_product_name() == "Sauce Labs Backpack"
            assert payment_page.get_price() == "$29.99"
            assert payment_page.get_quantity() == "1"
            assert payment_page.get_payment_info()
            assert payment_page.get_shipping_info()
            assert "$29.99" in payment_page.get_subtotal()
            assert payment_page.get_tax().startswith("Tax:")
            assert payment_page.get_total().startswith("Total:")
            assert payment_page.verify_finish_button()
            assert payment_page.verify_cancel_button()
            payment_page.click_finish_button()

        with allure.step("Verify order confirmation and log out"):
            confirmation_page = OrderConfirmationPage(page)
            assert confirmation_page.get_current_url().endswith("/checkout-complete.html")
            assert confirmation_page.get_dashboard_text() == "Swag Labs"
            assert confirmation_page.get_order_status() == "Checkout: Complete!"
            assert "Your order has been dispatched" in confirmation_page.get_success_message()
            confirmation_page.download_pdf_order()
            confirmation_page.hamburger_menu()
            confirmation_page.logout()
            assert "saucedemo.com" in page.url
