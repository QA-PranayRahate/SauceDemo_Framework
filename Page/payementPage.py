

class PayementPage:
    def __init__(self,page):
        self.page=page
        self.product_name=self.page.locator('[data-test="inventory-item-name"]')
        self.price=self.page.locator('[data-test="inventory-item-price"]')
        self.quantity=self.page.locator('[data-test="item-quantity"]')
        self.payement_info=self.page.locator('[data-test="payment-info-value"]')
        self.shipping_info=self.page.locator('[data-test="shipping-info-value"]')
        self.subtotal=self.page.locator('[data-test="subtotal-label"]')
        self.tax=self.page.locator('[data-test="tax-label"]')
        self.total=self.page.locator('[data-test="total-label"]')
        self.Finish_button=self.page.get_by_text('Finish')
        self.Cancel_button=self.page.get_by_text('Cancel')

    def get_current_url(self):
        return self.page.url
    
    def get_product_name(self):
        return self.product_name.inner_text()

    def get_price(self):
        return self.price.inner_text()

    def get_quantity(self):
        return self.quantity.inner_text()

    def get_payment_info(self):
        return self.payement_info.inner_text()

    def get_shipping_info(self):
        return self.shipping_info.inner_text()

    def get_subtotal(self):
        return self.subtotal.inner_text()

    def get_tax(self):
        return self.tax.inner_text()

    def get_total(self):
        return self.total.inner_text()

    def verify_finish_button(self):
        return self.Finish_button.is_visible()

    def verify_cancel_button(self):
        return self.Cancel_button.is_visible()

    def click_finish_button(self):
            self.Finish_button.click()

