from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage


class CartPage(BasePage):
    cart_empty_txt = 'Your cart is empty'

    CART_TOTAL = (By.XPATH, "//span[contains(@class,'sc-4625')]")
    CART_EMPTY_MESSAGE = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_cart_empty(self):
        actual = self.verify_text(self.cart_empty_txt,*self.CART_EMPTY_MESSAGE)
        assert self.cart_empty_txt in actual, f"{self.cart_empty_txt} but got {actual}"
        print("Actual cart message:", actual )
        sleep(5)

    def cart_items_verified(self, amount):
        cart_summary = self.driver.find_element(*self.CART_TOTAL).text.lower()
        expected_text = f"subtotal ({amount} item"
        assert expected_text in cart_summary, f"Expected '{expected_text}' but got '{cart_summary}'"