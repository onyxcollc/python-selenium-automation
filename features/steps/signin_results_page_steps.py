from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@when('Enter email {address}')
def enter_email_address(context, address):
    context.app.signin_page.enter_email_address(address)

@when('Click continue button')
def click_continue_button(context):
    context.app.signin_page.click_continue_button()


@when('CLick enter your password')
def click_password_button(context):
    context.app.signin_page.click_password_button()


@when('Enter your {password}')
def enter_password(context,password):
    context.app.signin_page.enter_password_text(password)


@when('Click sign in with password')
def click_sign_in(context):
    context.app.signin_page.click_sign_in_with_password()

@then('Verify sign in result')
def verify_sign_in(context):
    # element = context.driver.find_element(*SIGN_IN_RESULT)
    # actual_text = element.text
    # assert 'Sign in or create account'in actual_text, f"Error, expected 'Sign in or create account' in actual text: {actual_text}"
    context.app.signin_page.verify_sign_in()


# @then('Verify login')
# def verify_log_in(context):
#     context.app.sign_in_page.verify_login()