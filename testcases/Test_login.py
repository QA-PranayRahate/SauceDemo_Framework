import json
from pathlib import Path

import pytest
import allure

with Path(__file__).with_name('login_details.json').open(encoding='utf-8') as login_details_file:
    LOGIN_DETAILS = json.load(login_details_file)

TEST_USERS = [
    (LOGIN_DETAILS['username'], LOGIN_DETAILS['password']),
]

@pytest.mark.regression
class TestLogin:
    @pytest.mark.parametrize('username,password', TEST_USERS)
    def test_login(self,page,username,password,homepage):
        with allure.step("Verify successful login and inventory page"):
            assert 'https://www.saucedemo.com/inventory.html' in homepage.get_current_url()
            assert 'Swag Labs' in homepage.get_dashboard_text()




