from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep






HEADER_LINKS =(By.CSS_SELECTOR, "[data-test*= '@web/GlobalHeader/UtilityHeader/']")



@when('Search for {search_word}')
def search_product(context,search_word):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    # context.driver.wait.until(EC.visibility_of_element_located(*SEARCH_BUTTON)).click()
    # sleep(5)
    context.app.header.search_product(search_word)


@when('Click search button')
def click_search(context):
    # context.driver.find_element(*SEARCH_BUTTON).click()
    # sleep(5)
    context.app.header.click_search()


@when('Click account icon')
def click_account_icon(context):
    # context.driver.find_element(*ACCOUNT_ICON).click()
    context.app.header.click_account_icon()


@when('Click on cart icon')
def cart_icon_click(context):
    # context.driver.find_element(*CART_ICON).click()
    # sleep(5)
    context.app.header.click_cart()


@when('Click sign in button')
def click_sign_in_button(context):
    # context.driver.find_element(*SIGN_IN_BUTTON).click()
    # sleep(3)
    context.app.header.click_sign_in_button()

@then('Verify header has {number} links')
def verify_header_links(context,number):
   links = context.driver.find_elements(*HEADER_LINKS)
   print(links)

   assert len(links) == int(number), f"Expected {number}links, got {len(links)}"
