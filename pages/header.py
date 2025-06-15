from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.XPATH, "//input[@type='search']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")


    def search_product(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(10)

    def click_cart(self):
        self.click(*self.CART_ICON)