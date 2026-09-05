

class CartPage:
    def __init__(self,page):
        self.page=page

        self.view_cart_button= self.page.locator('.shopping_cart_link')
        self.quantity=self.page.locator('[data-test="item-quantity"]')
        self.item_name=self.page.get_by_text('Sauce Labs Backpack')
        self.price=self.page.locator('[data-test="inventory-item-price"]')
        self.remove_button=self.page.get_by_text('Remove')
        self.checkout_button=self.page.get_by_text('Checkout')

        
    def view_cart(self):
        self.view_cart_button.click()

    def get_quantity(self):
        return self.quantity.inner_text()

    def get_item_name(self):
        return self.item_name.inner_text()

    def get_price(self):
        return self.price.inner_text()
    
    def remove_item(self):
        return self.remove_button

    def has_item(self):
        return self.item_name.is_visible()

    def get_checkout_button(self):
        return self.checkout_button

    def click_checkout_button(self):
        self.checkout_button.click()    

    