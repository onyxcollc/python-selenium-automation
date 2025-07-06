from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class ProductDetailsPage(BasePage):

    COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class='styles_ndsCarouselItem__dnUkr']")
    SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='styles_headerWrapper__']")

    def open_product_details_page(self, product):
        self.get(f'https://www.target.com/p/{product}')


    def verify_user_colors(self):
        expected_colors = ['Black', 'Dark Blue', 'Dark Green', 'Light Gray', 'Light Green',
                           'light Green','Railroad Gray', 'Red Velvet','True White'
                           ,'Blue', 'Pink','Aqua Green']
        actual_colors = []

        colors = self.find_elements(*self.COLOR_OPTIONS)  # webelements1, webelements2, webelements3
        print(colors)

        for color in colors:
            color.click()
            sleep(4)

            selected_color = self.find_element(*self.SELECTED_COLOR).text
            print("Current color:", selected_color)

            selected_color = selected_color.split('\n')[1]
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f"Error, expected {expected_colors} did not match actual {actual_colors}"
