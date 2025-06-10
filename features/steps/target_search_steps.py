from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
    search_box = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='search']")))

    search_box.send_keys('tea')

    search_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))

    search_button.click()


@then('Verify search worked')
def verify_search(context):
    result_text_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-test='lp-resultsCount']")))

    actual_text = result_text_element.text
    assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"



@when('Click on cart icon')
def cart_icon_click(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='@web/CartLink']").click()
    sleep(5)

@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart(context):
    element = context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt")
    actual_text = element.text
    assert 'Your cart is empty' in actual_text, f"Error, expected 'Your cart is empty' in actual text: {actual_text}"


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