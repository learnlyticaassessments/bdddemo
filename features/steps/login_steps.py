from behave import given, when, then
from pages.login_page import LoginPage

@given("the user is on the login page")
def step_open_login(context):
    context.login_page = LoginPage(context.page, context.base_url)
    context.login_page.open()

@when('the user logs in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)

@then("the dashboard should be visible")
def step_verify_dashboard(context):
    assert context.login_page.is_dashboard_visible(), "Dashboard was not visible after login"
