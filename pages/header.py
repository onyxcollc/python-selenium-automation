from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    ACCOUNT_ICON = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    SEARCH_FIELD = (By.XPATH, "//input[@type='search']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@data-test='accountNav-signIn']")
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")


    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(10)


    def click_search(self):
        self.wait_for_element_click(*self.SEARCH_BUTTON)


    def click_cart(self):
        # self.click(*self.CART_ICON)
        self.wait_for_element_click(*self.CART_ICON)


    def click_sign_in_button(self):
        self.wait_for_element_click(*self.SIGN_IN_BUTTON)


    def click_account_icon(self):
        self.wait_for_element_click(*self.ACCOUNT_ICON)


    # def verify_header_links(self):
    #     self.verify_text(*self.)

