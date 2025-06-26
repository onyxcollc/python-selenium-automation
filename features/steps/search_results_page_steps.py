from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



SEARCH_RESULT_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")


PRODUCT_LISTINGS = (By.CSS_SELECTOR,"[class='container clearfix']")
PRODUCT_TITLE = (By.CSS_SELECTOR,"[title*='Xbox']")
PRODUCT_IMG = (By.CSS_SELECTOR,'img')




@when('Click on Add to Cart button')
def click_add_to_cart(context):
    #context.driver.execute_script("window.scrollTo(0, 500);")
    # context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    # #add_button = WebDriverWait(context.driver,14).until(EC.element_to_be_clickable(ADD_TO_CART_BUTTON))
    #
    # #add_button.click()
    # sleep(8)
    context.app.search_results_page.click_add_to_cart()

@when('Store product name')
def store_product_name(context):
    # context.driver.execute_script("window.scrollTo(0, 500);")
    # context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    # print('Product name stored ', context.product_name)
    context.app.cart_page.store_product_name()

@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart_side_nav(context):
    #context.driver.wait.until(EC.element_to_be_selected(*ADD_TO_CART_BUTTON_SIDE_NAV)).click()
    # context.driver.find_element(*ADD_TO_CART_BUTTON_SIDE_NAV).click()
    # sleep(5)
    context.app.main_page.confirm_add_to_cart_side_nav()



@when('Hover over favorites icon')
def hover_favorites_icon(context):
    context.app.search_results_page.hover_fav_icon()


@then('Verify search worked for {product}')
def verify_search(context, product):
    # actual_text = context.driver.find_element(*SEARCH_RESULT_TXT).text
    # assert product in actual_text, f"Error, expected text {product} not in actual {actual_text}"
    context.app.search_results_page.verify_search_results(product)


@then('Verify that every product has a name and an image')
def verify_name_and_image(context):

    products = context.driver.find_elements(*PRODUCT_LISTINGS)

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)


@then('Favorites tooltip is shown')
def verify_fav_tt_shown(context):
    context.app.search_results_page.verify_fav_tt_shown()