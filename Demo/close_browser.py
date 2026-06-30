# from pydoc import

from playwright.sync_api import sync_playwright, Playwright
import random

pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://playwright.dev/python/docs/api/class-playwright#methods")
print(f"Page title : {page.title()}")
ss_num = random.randint(1000,9999)
page.screenshot(path=f"ScreenShot\SS_{ss_num}.png")
# browser.close()






