# features/environment.py
from playwright.sync_api import sync_playwright

def before_all(context):
    context._pw = sync_playwright().start()
    context._browser = context._pw.chromium.launch(headless=True)

def before_scenario(context, scenario):
    context.page = context._browser.new_page()
    context.base_url = "https://www.saucedemo.com"

def after_scenario(context, scenario):
    # Only close if it exists (prevents teardown crashes)
    if hasattr(context, "page") and context.page:
        context.page.close()

def after_all(context):
    if hasattr(context, "_browser") and context._browser:
        context._browser.close()
    if hasattr(context, "_pw") and context._pw:
        context._pw.stop()
