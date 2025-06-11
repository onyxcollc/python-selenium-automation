from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@when('Search for {product}')
def search_product(context,product):
    context.driver.find_element(By.XPATH,"//input[@type='search']").send_keys(product)
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()



@when('Click on cart icon')
def cart_icon_click(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(5)


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    sleep(13)
    context.driver.execute_script("window.scrollTo(0, 500);")
    # context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);)")
    context.driver.find_element(By.CSS_SELECTOR,"[id*='addToCartButton']").click()
    sleep(5)

@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    WebDriverWait(context.driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[class*='contentWrapper']")))


    button = WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test='shippingButton']")))

    print("Add to Cart button found")
    button.click()

@when('Click account icon')
def click_account_icon(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()

@when('Click sign in button')
def click_sign_in_button(context):
    context.driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
    sleep(3)


@then('Verify header has {number} links')
def verify_header_links(context,number):
   links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*= '@web/GlobalHeader/UtilityHeader/']")
   print(links)

   assert len(links) == int(number), f"Expected {number}links, got {len(links)}"
