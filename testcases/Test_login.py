import pytest
import allure

@pytest.mark.regression
@pytest.mark.run(order=1)
class TestLogin:
    def test_login(self, loginpage, login_credentials, homepage):
        username, password = login_credentials
        with allure.step("Verify successful login and inventory page"):
            loginpage.login_as_standard_user(username, password)
            assert 'https://www.saucedemo.com/inventory.html' in homepage.get_current_url()
            assert 'Swag Labs' in homepage.get_dashboard_text()
