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
