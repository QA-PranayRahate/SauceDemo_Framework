import pytest
import allure

@pytest.mark.regression
class TestAddToCartPage:


    def test_verify_url_once_logged_in(self,productpage):
        with allure.step("Verify product URL"):
            assert 'https://www.saucedemo.com/inventory-item.html?id=4' in productpage.get_current_url()

    def test_add_product_to_cart(self,productpage):
        with allure.step("Add backpack to cart"):
            assert productpage.add_to_cart_button.is_visible()
            productpage.add_product_to_cart()
            assert productpage.is_product_added()


    def test_dashboard_text(self, productpage):
        with allure.step("Verify product page dashboard"):
            assert "Swag Labs" in productpage.get_dashboard_text()

    def test_product_name(self, productpage):
        with allure.step("Verify product name"):
            product_text = productpage.get_product_name()
            assert "Sauce Labs Backpack" in product_text

    def test_product_price(self, productpage):
        with allure.step("Verify product price"):
            actual_price = productpage.get_product_price()
            assert "$29.99" in actual_price
 
 


    