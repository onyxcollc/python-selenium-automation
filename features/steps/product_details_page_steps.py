from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




@given('Open target product {product} page')
def open_target(context, product):
    context.app.product_details_page.open_product_details_page(product)

@then('Verify user can click through colors')
def click_verify_user_colors(context):
    context.app.product_details_page.verify_user_colors()