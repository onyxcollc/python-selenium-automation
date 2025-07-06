from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.google.com")

driver.find_element(By.XPATH,'......').text
driver.find_element(By.CSS_SELECTOR,'.......').click()
driver.find_element(By.CSS_SELECTOR,'.......').send_keys("jdfndsj s ")
