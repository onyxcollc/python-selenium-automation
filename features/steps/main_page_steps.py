from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep





@given('Open target main page')
def open_target_main_page(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()