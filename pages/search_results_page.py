from selenium.webdriver.common.by import By

from pages.base_page import BasePage




class SearchResultsPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@style='display: inline-block;']//button[@type='button']")
    SEARCH_RESULT_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")




    def verify_search_results(self,product):
        self.verify_partial_text(product,*self.SEARCH_RESULT_TXT)


    def click_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BUTTON)


