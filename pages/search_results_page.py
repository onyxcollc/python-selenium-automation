from selenium.webdriver.common.by import By

from pages.base_page import BasePage




class SearchResultsPage(BasePage):

    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@style='display: inline-block;']//button[@type='button']")
    SEARCH_RESULT_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    FAV_ICON = (By.CSS_SELECTOR,"button[data-test='FavoritesButton']")
    FAV_TT_TEXT = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")

    PRODUCT_LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.XPATH, "//div[contains(@title,'Controller')]")
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


    def verify_search_results(self,product):
        self.verify_partial_text(product,*self.SEARCH_RESULT_TXT)


    def click_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BUTTON)


    def hover_fav_icon(self):
        self.hover_element(*self.FAV_ICON)


    def verify_fav_tt_shown(self):
        self.find_element(*self.FAV_TT_TEXT)


    def verify_name_and_image(self):
        products = self.driver.find_elements(*self.PRODUCT_LISTINGS)[:8]

        for product in products:
            title = product.find_elements(*self.PRODUCT_TITLE)

            assert title, 'Product title not shown'

            product.find_element(*self.PRODUCT_IMG)

