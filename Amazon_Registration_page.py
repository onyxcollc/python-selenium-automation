from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#creating the driver.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#open the Amazon url
driver.get('https://www.amazon.com/ap/register?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&showRememberMe=true&openid.pape.max_auth_age=0&pageId=usflex&prepopulatedLoginId=&openid.assoc_handle=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%3Fref_%3Dnav_signin&policy_handle=Retail-Checkout')


#Click the continue button
driver.find_element(By.CSS_SELECTOR,".a-button-input").click()


#Prcoceed to Create an Account
driver.find_element(By.CSS_SELECTOR,".a-button-input").click()

#Check Logo
driver.find_element(By.CSS_SELECTOR,"i.a-icon.a-icon-logo")

# Create account text
driver.find_element(By.CSS_SELECTOR,".a-spacing-small")

# "Your Name" Space
driver.find_element(By.CSS_SELECTOR,"#ap_customer_name")

# Password Space
driver.find_element(By.CSS_SELECTOR,"#ap_password")

#  Re-enter Space
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")

# Continue Button
driver.find_element(By.CSS_SELECTOR,"#continue")

#Sign  In  Instead
driver.find_element(By.XPATH,"//a[contains(@href,'/ap/sign')]")

#Conditions of Use Link
driver.find_element(By.XPATH,"//a[contains(@href,'_notification_condition')]")

#Privacy Notice Link
driver.find_element(By.XPATH,"//a[contains(@href,'_notification_privacy')]")

sleep(5)

print("Test Passed")



