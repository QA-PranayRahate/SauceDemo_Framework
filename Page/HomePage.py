

class HomePage:
    def __init__(self,page):
        self.page=page
        self.dashboard_swag_labs_text = self.page.locator('.app_logo')
      
    def get_current_url(self):
        return self.page.url
    
    def get_dashboard_text(self):
        return self.dashboard_swag_labs_text.inner_text()


    