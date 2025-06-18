from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


#CART_TOTAL = (By.XPATH,"//span[contains(@class,'sc-4625')]")


@when('Open cart page')
def open_cart_page(context):
    # context.driver.get('https://www.target.com/cart')
    context.app.main_page.open_cart_page()

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    # cart_summery = context.driver.find_element(*CART_TOTAL).text
    # assert f'subtotal{amount}' in cart_summery, f"Expected {amount} item(s) but got {cart_summery}"
    # context.driver.wait.unti(EC.text_to_be_present_in_element(*PRODUCT_NAME))
    context.app.cart_page.verify_cart_items(amount)

@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart(context):
    # element = context.driver.find_element(*CART_EMPTY_MESSAGE)
    # actual_text = element.text
    # assert 'Your cart is empty' in actual_text, f"Error, expected 'Your cart is empty' in actual text: {actual_text}"
    context.app.cart_page.verify_cart_empty()

@then('Verify cart has correct product')
def verify_product_correct(context):
    # # context.product_name => stored before to use later
    # product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text.strip()
    # stored_name = context.product_name.strip()

    # assert "portmeirion botanic" in product_name_in_cart.lower(), \
    # f"Cart product '{product_name_in_cart}' is not the expected product."

    # assert stored_name[:20].lower() in product_name_in_cart[:30].lower(), \
    #     f"Expected start '{stored_name[:20]}' to match cart '{product_name_in_cart[:30]}'"

    #sleep(5)
    context.app.cart_page.verify_product_correct()



@then('Verify Cart page opened')
def verify_cart_opened(context):
        context.app.cart_page.verify_cart_opened()
