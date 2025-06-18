from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class MainPage(BasePage):

    ADD_TO_CART_BUTTON_SIDE_NAV = (By.XPATH, "//button[@data-test='shippingButton']")

    def open_main_page(self):
        self.driver.get("https://www.target.com/")



    def open_cart_page(self):
        self.driver.get('https://www.target.com/cart')


    def confirm_add_to_cart_side_nav(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BUTTON_SIDE_NAV)