import datetime

from playwright.sync_api import sync_playwright

def test_handle_page():
    with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=True,args=['--start-maximized'])
        context=browser.new_context(no_viewport=True)
        page=context.new_page()

        page.goto('https://testautomationpractice.blogspot.com/#')

        with page.expect_popup() as new_page:
            page.get_by_role('button',name='New Tab').click()
            newpage=new_page.value
            ld=newpage.get_by_text('SDET-QA Blog')
            print(ld.inner_text())
            rows=newpage.locator('#crosscol a').all()
            for index,row in enumerate(rows):
                all_links=row.get_attribute('href')
                print(f'{index+1} - {all_links}')
            newpage.close()

def test_handle_download():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, args=['--start-maximized'])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto('https://demo.automationtesting.in/FileDownload.html')

        with page.expect_download() as download_info:
            page.get_by_role('link',name='Download').click()
            download=download_info.value
            date_now=datetime.datetime.now().strftime("%Y-%m-%d_%H")
            download.save_as(f'selenium_guide{date_now}.pdf')




