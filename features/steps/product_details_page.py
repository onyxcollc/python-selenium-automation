from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR,"li[class*='styles_']")
SELECTED_COLOR = (By.CSS_SELECTOR,"div[class*='styles_headerWrapper']"  )

@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/women-s-short-sleeve-graphic-t-shirt-universal-thread/-/{product_id}?preselect=94336503#lnk=sametab')
    sleep(8)

@then('Verify user can click through colors')
def click_verify_user_colors(context):
    expected_colors =['Cream Letters', 'Navy Blue Letters', 'Red Letters','White Letters']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS) # webelements1, webelements2, webelements3
    print(colors)

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print("Current color:", selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f"Error, expected {expected_colors} did not match actual {actual_colors}"
