from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify signin form opened')
def verify_sign_in(context):
    element = context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt")
    actual_text = element.text
    assert 'Sign in or create account'in actual_text, f"Error, expected 'Sign in or create account' in actual text: {actual_text}"