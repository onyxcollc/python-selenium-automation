from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGN_IN_RESULT = (By.CSS_SELECTOR,"[class*=ndsHeading]")


@then('Verify signin form opened')
def verify_sign_in(context):
    element = context.driver.find_element(*SIGN_IN_RESULT)
    actual_text = element.text
    assert 'Sign in or create account'in actual_text, f"Error, expected 'Sign in or create account' in actual text: {actual_text}"