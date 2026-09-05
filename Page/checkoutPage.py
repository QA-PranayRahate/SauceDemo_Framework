
class CheckoutPage:
    def __init__(self,page):
        self.page=page

        self.first_name=self.page.get_by_placeholder('First Name')
        self.last_name=self.page.get_by_placeholder('Last Name')
        self.postal_code=self.page.get_by_placeholder('Zip/Postal Code')
        self.continue_button=self.page.get_by_text('Continue')

    def get_current_url(self):
        return self.page.url

    def enter_first_name(self,first_name):
        self.first_name.fill(first_name)

    def enter_last_name(self,last_name):
        self.last_name.fill(last_name)

    def enter_postal_code(self,postal_code):
        self.postal_code.fill(postal_code)

    def click_continue_button(self):
        self.continue_button.click()