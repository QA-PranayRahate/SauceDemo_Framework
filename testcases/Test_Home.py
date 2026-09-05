import pytest
import allure
@pytest.mark.regression
class Test_HomePage:


    def test_current_url(self,homepage):
        with allure.step("Verify inventory URL"):
            assert 'https://www.saucedemo.com/inventory.html' in homepage.get_current_url()

    def test_dashboard_text(self, homepage):
        with allure.step("Verify dashboard title"):
            assert "Swag Labs" in homepage.get_dashboard_text()
