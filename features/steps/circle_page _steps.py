from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep





@given('Open target circle page')
def open_circle_page(context):
    context.app.circle_page.open_circle_page()


@then('Verify circle page has more then {number} benefit cells')
def verify_benefit_cells(context,number):
    context.app.circle_page.verify_benefit_cells(number)