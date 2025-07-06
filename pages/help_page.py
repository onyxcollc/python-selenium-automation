from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import BasePage


class HelpPage(BasePage):

    # RETURNS_HEADER = (By.XPATH, "//h1[text()=' Returns']")
    # PROMOTIONS_HEADER = (By.XPATH, "//h1[text()=' Current promotions']")
    SELECT_DD = (By.CSS_SELECTOR, "select[id*='viewHelpTopics']")
    HEADER = (By.XPATH,"//h1[text()=' {SUBSTR}']")

    # Dynamic locator => generating locator during TestCase execution
    # if expected_text = Returns:
    # (By.XPATH,"//h1[text()=' {SUBSTR}']") => (By.XPATH, "//h1[text()=' Returns']")
    def _get_header_locator(self, expected_text):
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTR}', expected_text)]


    def open_help_page(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery=')




    def select_help_topics(self,value):
        dd = self.find_element(*self.SELECT_DD)
        select = Select(dd)
        select.select_by_value(value)


    def verify_page_header(self,expected_text):
        locator = self._get_header_locator(expected_text)
        self.wait_for_element(*locator)


    # def verify_returned_opened(self):
    #     self.find_element(*self.RETURNS_HEADER)
    #
    # def verify_promotions_coupons_opened(self):
    #     self.find_element(*self.PROMOTIONS_HEADER)



