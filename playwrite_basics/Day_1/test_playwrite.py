from playwright.sync_api import Page, expect

def test_verifyPageURL(page:Page):
    # page is built-in fixture provided by play-wright.
    # page fixture is belong to Page class which is present in sync_api package.
    # By default play-write will follow Chromium(chrome or edge) browser.
    # pytest will have their own assertion.
    # but while play-write scripting we have to use play-write assertions.

    page.goto("https://www.automationpractice.pl/index.php")
    expect(page).to_have_url("https://www.automationpractice.pl/index.php")








