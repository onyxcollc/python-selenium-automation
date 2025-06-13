from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.XPATH, "//input[@type='search']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    def search_product(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
