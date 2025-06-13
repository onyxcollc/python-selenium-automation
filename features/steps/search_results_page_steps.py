from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



SEARCH_RESULT_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,"[id*='addToCartButton']")
ADD_TO_CART_BUTTON_SIDE_NAV = (By.CSS_SELECTOR,"[class*='contentWrapper']")
SIDE_NAV_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,"[data-test='shippingButton']")
SIDE_NAV_PRODUCT_NAME = (By.XPATH,"//h4[contains(text(),'Dad Nutrition Facts Mug')]")


@when('Click on cart icon')
def cart_icon_click(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME)).click()


@when('Store product name')
def store_product_name(context):
    context.driver.execute_script("window.scrollTo(0, 500);")
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored ', context.product_name)




@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_selected(*ADD_TO_CART_BUTTON_SIDE_NAV)).click()
     #context.driver.find_element(*ADD_TO_CART_BUTTON).click()



@then('Verify search worked for {product}')
def verify_search(context, product):
    actual_text = context.driver.find_element(*SEARCH_RESULT_TXT).text
    assert product in actual_text, f"Error, expected text {product} not in actual {actual_text}"


