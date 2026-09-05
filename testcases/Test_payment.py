import pytest
import allure

@pytest.mark.regression
class Test_payement:

    def test_current_url(self,paymentpage):
        with allure.step("Verify payment URL"):
            assert 'https://www.saucedemo.com/checkout-step-two.html' in paymentpage.get_current_url()
    def test_product_name(self, paymentpage):
        with allure.step("Verify payment product name"):
            product_name = paymentpage.get_product_name()
            print(f"Product name: {product_name}")
            assert product_name == "Sauce Labs Backpack"

    def test_price(self, paymentpage):
        with allure.step("Verify payment price"):
            price = paymentpage.get_price()
            print(f"Price: {price}")
            assert price == "$29.99"

    def test_quantity(self, paymentpage):
        with allure.step("Verify payment quantity"):
            quantity = paymentpage.get_quantity()
            print(f"Quantity: {quantity}")
            assert quantity == "1"

    def test_payment_info(self, paymentpage):
        with allure.step("Verify payment information"):
            payment_info = paymentpage.get_payment_info()
            print(f"Payment info: {payment_info}")
            assert payment_info

    def test_shipping_info(self, paymentpage):
        with allure.step("Verify shipping information"):
            shipping_info = paymentpage.get_shipping_info()
            print(f"Shipping info: {shipping_info}")
            assert shipping_info

    def test_subtotal(self, paymentpage):
        with allure.step("Verify subtotal"):
            subtotal = paymentpage.get_subtotal()
            print(f"Subtotal: {subtotal}")
            assert "$29.99" in subtotal

    def test_tax(self, paymentpage):
        with allure.step("Verify tax"):
            tax = paymentpage.get_tax()
            print(f"Tax: {tax}")
            assert tax.startswith("Tax:")

    def test_total(self, paymentpage):
        with allure.step("Verify total"):
            total = paymentpage.get_total()
            print(f"Total: {total}")
            assert total.startswith("Total:")

    def test_finish_button(self, paymentpage):
        with allure.step("Verify finish button"):
            finish_visible = paymentpage.verify_finish_button()
            print(f"Finish button visible: {finish_visible}")
            assert finish_visible

    def test_cancel_button(self, paymentpage):
        with allure.step("Verify cancel button"):
            cancel_visible = paymentpage.verify_cancel_button()
            print(f"Cancel button visible: {cancel_visible}")
            assert cancel_visible