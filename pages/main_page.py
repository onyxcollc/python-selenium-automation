from pages.base_page import BasePage


class MainPage(BasePage):

    def open_main_page(self):
        self.driver.get("https://www.target.com/")
