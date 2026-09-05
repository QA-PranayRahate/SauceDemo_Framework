class ProductPage:
    def __init__(self, page):
        self.page = page
        self.dashboard_text=self.page.get_by_text('Swag Labs')
        self.product_name = self.page.get_by_text('Sauce Labs Backpack')
        self.product_price = self.page.get_by_text('$29.99', exact=True)
        self.add_to_cart_button = self.page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"], '
            '[data-test="add-to-cart"]'
        )
        self.remove_button = self.page.get_by_text('Remove')


    def click_product_by_name(self):
        self.product_name.click()

    def get_current_url(self):
        return self.page.url

    def get_dashboard_text(self):
        return self.dashboard_text.inner_text()
    
    def is_product_added(self):
        return self.remove_button.is_visible()

    def get_product_name(self):
        return self.product_name.inner_text()  
 
    
    def get_product_price(self):
        return self.product_price.inner_text()
    
    def add_product_to_cart(self):
        self.add_to_cart_button.click()


    


