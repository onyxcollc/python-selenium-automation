from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def cart_icon_click(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='@web/CartLink']").click()
    sleep(5)

@then('Verify cart is empty')
def verify_empty_cart(context):
    element = context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt")
    actual_text = element.text
    assert 'Your cart is empty' in actual_text, f"Error, expected 'Your cart is empty' in actual text: {actual_text}"