from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


HELP_PAGE_ELEMENTS = (By.CSS_SELECTOR,"a[class*='styles_ndsLink']")

@given('Go to help page')
def help_page_link(context):
    context.driver.get('https://help.target.com/help')


@given('Open Help page for Returns')
def open_help_page(context):
    context.app.help_page.open_help_page()



@when('Select Help topic {value}')
def select_promotions_coupons(context, value):
    context.app.help_page.select_help_topics(value)


@then('Verify help {expected_header_text} page opened')
def verify_help_page_opened(context,expected_header_text):
    context.app.help_page.verify_page_header(expected_header_text)


@then('Verify elements on the page')
def verify_elements(context):
    elements = context.driver.find_elements(*HELP_PAGE_ELEMENTS)
    assert elements, "Expected at least one element with class 'container clearfix' but found none"



    # @then('Verify help Returns page opened')
    # def verify_returned_opened(context):
    #     context.app.help_page.verify_returned_opened()
    #
    #
    # @then('Verify help Current promotions page opened')
    # def verify_promotions_coupons_opened(context):
    #     context.app.help_page.verify_promotions_coupons_opened()