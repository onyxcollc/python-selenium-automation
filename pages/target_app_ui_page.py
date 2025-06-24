from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TargetAppUiPage(BasePage):

    PP_LINK = (By.CSS_SELECTOR,"a[aria-label*='privacy policy']")


    def open_target_app(self):
        self.driver.get('https://www.target.com/c/target-app/-/N-4th2r')


    def click_privacy_link(self):
        self.click(*self.PP_LINK)

 