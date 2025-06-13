from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SEARCH_FIELD = (By.XPATH,"//input[@type='search']")
SEARCH_BUTTON =(By.XPATH,"//button[@type='submit']")
ACCOUNT_ICON = (By.XPATH,"//a[@data-test='@web/AccountLink']")
SIGN_IN_BUTTON = (By.XPATH,"//button[@data-test='accountNav-signIn']")
HEADER_LINKS =(By.CSS_SELECTOR, "[data-test*= '@web/GlobalHeader/UtilityHeader/']")



@when('Search for {search_word}')
def search_product(context,search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.wait.until(EC.presence_of_element_located(*SEARCH_BUTTON)).click()


@when('Click account icon')
def click_account_icon(context):
    context.driver.find_element(*ACCOUNT_ICON).click()

@when('Click sign in button')
def click_sign_in_button(context):
    context.driver.find_element(*SIGN_IN_BUTTON).click()
    sleep(3)


@then('Verify header has {number} links')
def verify_header_links(context,number):
   links = context.driver.find_elements(*HEADER_LINKS)
   print(links)

   assert len(links) == int(number), f"Expected {number}links, got {len(links)}"
