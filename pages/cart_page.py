from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage


class CartPage(BasePage):
    # Copy
    cart_empty_txt = 'Your cart is empty'

    # Locators
    CART_TOTAL = (By.XPATH, "//span[contains(@class,'sc-4625')]")
    CART_EMPTY_MESSAGE = (By.XPATH, "//h1[text()='Your cart is empty']")
    SIDE_NAV_PRODUCT_NAME = (By.XPATH, "//h4[contains(text(),'Portmeirion Botanic')]")

    PRODUCT_NAME = (By.XPATH,"//div[contains(text(),'Portmeirion Botanic')]")



    def store_product_name(self):
        self.verify_partial_text('Portmeirion Botanic',*self.SIDE_NAV_PRODUCT_NAME)


    def verify_cart_empty(self):
       self.verify_text(self.cart_empty_txt,*self.CART_EMPTY_MESSAGE)


    def verify_cart_items(self, amount):
        # cart_summary = self.driver.find_element(*self.CART_TOTAL).text.lower()
        # expected_text = f"subtotal ({amount} item"
        # assert expected_text in cart_summary, f"Expected '{expected_text}' but got '{cart_summary}'"
        self.verify_text(str(amount),*self.CART_TOTAL)

    def verify_product_correct(self):
        self.verify_partial_text('Portmeirion Botanic',*self.PRODUCT_NAME)


    def verify_cart_opened(self):
     # self.verify_url('https://www.target.com/cart')
     # self.verify_partial_url('/cart')
        self.wait_for_url_contains('/cart')