from playwright.sync_api import sync_playwright, Playwright
import random


def run_browser(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/python/docs/api/class-playwright#methods")
    print(f"Page title : {page.title()}")
    ss_num = random.randint(1000,9999)
    page.screenshot(path=f"ScreenShot\SS_{ss_num}.png")
    # browser.close()

with sync_playwright() as pw:
    run_browser(pw)





