from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#Create The Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#Open the url
driver.get("https://www.target.com/")



#Action
driver.find_element(By.XPATH,"//a[@aria-label='Account, sign in']").click()
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

sleep(5)

#Assert (Verification)
expected_text = 'Sign in or create account'
actual_text = driver.find_element(By.XPATH,"//h1[contains(@class,'styles_ndsHeading__HcGpD')]" ).text
driver.find_element(By.XPATH,"//div[@class='sc-609faf1c-2 dVggxh']//button[@type='button']")

assert expected_text in actual_text, f"Error, expected {expected_text} not in actual {actual_text}"
print("Test Passed")
driver.quit()

# learn how to scroll with these scripts
# context.driver.execute_script("window.scrollTo(0, 500);")
# context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);)")