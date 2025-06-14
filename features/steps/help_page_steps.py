from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


HELP_PAGE_ELEMENTS = (By.CSS_SELECTOR,"[class='container clearfix']")

@given('Go to help page')
def help_page_link(context):
    context.driver.get('https://help.target.com/help')
    sleep(6)

@then('Verify elements on the page')
def verify_elements(context):
    elements = context.driver.find_elements(*HELP_PAGE_ELEMENTS)
    assert elements, "Expected at least one element with class 'container clearfix' but found none"