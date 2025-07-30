from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver,10)

#open LV website
driver.get('https://us.louisvuitton.com/eng-us/homepage')

#close cookie window
cookie = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ucm-openButton.ucm-choice__yes")))
cookie.click()

#click menu tab
menu_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[aria-label='Navigation Menu']")))
menu_tab.click()


#click the Women tab
women_tab = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Women']")))
women_tab.click()


#click Accessories
Accessories = wait.until(EC.element_to_be_clickable((By.ID,'w-category-cat10155-button')))
Accessories.click()

#click Scarves
Scarves = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[href*='accessories/scarves']")))
Scarves.click()