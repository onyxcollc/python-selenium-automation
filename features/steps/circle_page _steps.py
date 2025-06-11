from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify circle page has more then {number} benefit cells')
def verify_benefit_cells(context, number):
   cells = context.driver.find_elements(By.CSS_SELECTOR,"div[class*='cell-item']")
   print(f"Found{len(cells)} cells")

   assert len(cells) > int(number), f"Expected more than {number}, but found {len(cells)} "