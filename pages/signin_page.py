from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class SignInPage(BasePage):


    EMAIL_ADDRESS_VALUE = (By.CSS_SELECTOR, "[inputmode='email']")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    PASSWORD_BUTTON =(By.ID, "password")
    PASSWORD_TEXT = (By.XPATH,"//input[@data-test='login-password']")
    SIGN_IN_WITH_PASSWORD_BTN = (By.ID,"login")
    SIGN_IN_RESULT = (By.CSS_SELECTOR, "[class*=ndsHeading]")
    LOGIN_VERIFICATION = (By.XPATH, "//button[text()='Sign in with password']")
    TERMS_CONDITIONS_LINK = (By.CSS_SELECTOR,"a[aria-label*='terms & conditions']")



    def open_signin_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')


    def enter_email_address(self, address):
        self.input_text(address,*self.EMAIL_ADDRESS_VALUE)


    def click_continue_button(self):
        self.wait_for_element_click(*self.CONTINUE_BUTTON)


    def click_password_button(self):
        self.wait_for_element_click(*self.PASSWORD_BUTTON)


    def click_terms_and_conditions(self):
        self.click(*self.TERMS_CONDITIONS_LINK)

    def enter_password_text(self,password):
        self.input_text(password,*self.PASSWORD_TEXT)


    def click_sign_in_with_password(self):
        self.wait_for_element_click(*self.SIGN_IN_WITH_PASSWORD_BTN)



    def verify_sign_in(self):
        self.verify_text('Sign in or create account',*self.SIGN_IN_RESULT)

    #def verify_login(self):
        # self.verify_text('Hi, Nico',*self.LOGIN_VERIFICATION)
        # sleep(5)