from playwright.sync_api import Page

class LoginPage:
   
    def __init__(self, page):
        self.page = page

     # Locators
    USERNAME_FIELD = 'Username'
    PASSWORD_FIELD = 'Password'
    LOGIN_BUTTON = 'Login'


    def login_as_standard_user(self, username, password):
        self.page.get_by_placeholder(self.USERNAME_FIELD).fill(username)
        self.page.get_by_placeholder(self.PASSWORD_FIELD).fill(password)
        self.page.get_by_role('button', name=self.LOGIN_BUTTON).click()
        self.page.wait_for_timeout(4000)


