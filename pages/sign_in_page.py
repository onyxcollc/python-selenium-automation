from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class SignInPage(BasePage):


    SIGN_IN_RESULT = (By.CSS_SELECTOR, "[class*=ndsHeading]")

    def verify_sign_in(self):
        self.verify_text('Sign in or create account',*self.SIGN_IN_RESULT)


