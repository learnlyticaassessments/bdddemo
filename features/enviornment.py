from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_url = "https://www.saucedemo.com"

def after_scenario(context, scenario):
    if hasattr(context, "page"):
        context.page.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()
