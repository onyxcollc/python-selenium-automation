from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver,20)
driver.implicitly_wait(10)


# open the url
driver.get('https://us.louisvuitton.com/eng-us/homepage?utm_source=google&utm_medium=cpc&utm_campaign=LV_FLG_USA_ALWON_CORP_Other_OnGoing_EC_BREX_GTAD_MUL_ENG_USD_EXTM&gad_source=1&gad_campaignid=220402029&gbraid=0AAAAADs-5BsuPJj2ad5BBe2bzVnv4g1Sh&gclid=EAIaIQobChMI5vLYvNqrjgMV7CKzAB0tOxOUEAAYASAAEgKwT_D_BwE&gclsrc=aw.ds')
sleep(1)

driver.find_element(By.CSS_SELECTOR, ".ucm-openButton.ucm-choice__yes").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '.lv-header-icon-burger__bars').click()
sleep(1)
driver.find_element(By.XPATH, "//*[text()='Men']").click()
sleep(1)
driver.find_element(By.ID, "m-category-cat10037-button").click()
sleep(1)
driver.find_element(By.XPATH, "//a[@href='/eng-us/men/shoes/all-shoes/_/N-t118ht95']").click()
sleep(3)

