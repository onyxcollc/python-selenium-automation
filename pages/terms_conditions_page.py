from pages.base_page import BasePage


class TermsConditionsPage(BasePage):

    def verify_tc_opened(self):
        self.wait_for_url_contains('terms-conditions')