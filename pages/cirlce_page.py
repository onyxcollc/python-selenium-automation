from selenium.webdriver.common.by import By


from pages.base_page import BasePage


BENEFIT_CELLS = (By.CSS_SELECTOR,"div[class*='cell-item']")



class CirclePage(BasePage):

    def open_circle_page(self):
        self.open_url('circle')


    def verify_benefit_cells(self, number):
       cells = self.driver.find_elements(*BENEFIT_CELLS)
       print(f"Found{len(cells)} cells")

       assert len(cells) > int(number), f"Expected more than {number}, but found {len(cells)} "