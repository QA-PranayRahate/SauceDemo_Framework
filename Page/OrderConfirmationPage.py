class OrderConfirmationPage:
    def __init__(self,page):
        self.page=page
        self.dashboard_text=self.page.locator('.app_logo')
        self.title=self.page.locator('[data-test="title"]')
        self.thank_you_text=self.page.locator('[data-test="complete-text"]')
        self.back_home_button=self.page.get_by_role('button',name='Back Home')
        self.hamburger=self.page.get_by_role('button',name='Open Menu')
        self.logout_button=self.page.get_by_text('Logout')


    def get_current_url(self):
        return self.page.url

    def get_dashboard_text(self):
        return self.dashboard_text.inner_text()

    def get_order_status(self):
        return self.title.inner_text()

    def get_success_message(self):
        return self.thank_you_text.inner_text()

    def hamburger_menu(self):
        self.hamburger.click()

    def logout(self):
        self.logout_button.click()

        
