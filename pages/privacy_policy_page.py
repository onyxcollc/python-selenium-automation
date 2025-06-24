

from pages.base_page import BasePage


class PrivacyPolicyPage(BasePage):

    def verify_pp_opened(self):
        self.wait_for_url_contains('target-privacy-policy')
