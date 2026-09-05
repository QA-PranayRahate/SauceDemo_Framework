from playwright.sync_api import sync_playwright
import re
from pathlib import Path
def test_download_selenium():
    with sync_playwright() as p:
        browser=p.chromium.launch(channel='msedge',headless=False,args=['--start-maximized'])
        context=browser.new_context(no_viewport=True)
        page=context.new_page()

        page.goto('https://www.selenium.dev/downloads/')
        page.reload()
        with page.expect_download() as download_info:
            page.get_by_role('link',name='^4.48.0$').filter(has_text=re.compile('^4.48.0$')).click()
            download=download_info.value
            Path("./downloads").mkdir(parents=True, exist_ok=True)
            download.save_as(path='./downloads/selenium-server-4.48.0.jar') 
        sd=page.locator('sd').all()
  