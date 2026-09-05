import pandas as pd
#
# file=r"C:\Projects\this.xlsx"
# df=pd.read_excel(file,sheet_name="Sheet1")
# print(df.head())



def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a,end=' ')
        temp=a
        a=b
        b = temp


fib(10)

from playwright.sync_api import sync_playwright,Page,Route

def lock_images(route:Route):
    if route.request.resource_type=='image':
        route.abort()
    else:
        route.continue_()

def test_something(page:Page):
    # page.route('**/*',lock_images)
    page.goto('https://www.pinterest.com/')
    page.evaluate('window.scrollTo(0,document.body.scrollHeight)')
    page.wait_for_timeout(3000)
    page.evaluate('window.scrollTo(0,500)')

    page.wait_for_timeout(3000)