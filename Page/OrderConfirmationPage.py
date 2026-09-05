from datetime import datetime
class OrderConfirmationPage:
    def __init__(self,page):
        self.page=page
        self.dashboard_text=self.page.locator('.app_logo')
        self.title=self.page.locator('[data-test="title"]')
        self.thank_you_text=self.page.locator('[data-test="complete-text"]')
        self.generate_pdf_order=self.page.get_by_role('button',name='Generate PDF order')
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

    def download_pdf_order(self):
        with self.page.expect_download() as download_info:
            self.generate_pdf_order.click()
        download=download_info.value
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"swag-labs-order-{timestamp}.pdf"

        download.save_as(f"./downloads/{filename}")
        return filename

    def hamburger_menu(self):
        self.hamburger.click()

    def logout(self):
        self.logout_button.click()

        
