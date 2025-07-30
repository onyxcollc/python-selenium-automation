from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver,10)
driver.implicitly_wait(10)

#open_url
driver.get("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery=")


#find Browse Help dropdown
dd = driver.find_element(By.CSS_SELECTOR, "select[id*=viewHelpTopic]")
select = Select(dd)
select.select_by_visible_text('Partner Programs')

#verify Partner Programs Pagr Opened
wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Partner Programs']")))
expected_result = 'Partner Programs'
actual_result = driver.find_element(By.XPATH, "//h2[text()='Partner Programs']").text
assert expected_result == actual_result, f"Error expected result {expected_result} not in actual result{actual_result}"

print('Test Passed')

