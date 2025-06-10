from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Click account icon')
def click_account_icon(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()

@when('Click sign in button')
def click_sign_in_button(context):
    context.driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
    sleep(3)

@then('Verify signin form opened')
def verify_sign_in(context):
    element = context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt")
    actual_text = element.text
    assert 'Sign in or create account'in actual_text, f"Error, expected 'Sign in or create account' in actual text: {actual_text}"