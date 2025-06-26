from pages.base_page import BasePage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.target_app_ui_page import TargetAppUiPage
from pages.product_details_page import ProductDetailsPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.signin_page import SignInPage
from pages.terms_conditions_page import TermsConditionsPage


class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.help_page = HelpPage(driver)
        self.target_app_ui_page = TargetAppUiPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.signin_page = SignInPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.terms_conditions_page = TermsConditionsPage(driver)