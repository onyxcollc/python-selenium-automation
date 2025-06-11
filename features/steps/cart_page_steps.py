from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summery = context.driver.find_element(By.XPATH,"//div[span[contains(text(),'subtotal')]]")
    assert f'{amount} item(s)' in cart_summery, f"Expected {amount} item(s) but got {cart_summery}"


@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart(context):
    element = context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt")
    actual_text = element.text
    assert 'Your cart is empty' in actual_text, f"Error, expected 'Your cart is empty' in actual text: {actual_text}"
