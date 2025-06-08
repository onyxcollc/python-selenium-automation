from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#creating the driver.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

 #locator Continue
driver.find_element(By.XPATH,"//input[@class='a-button-input']" )

#locator Amazon logo
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
 
#locator Email
driver.find_element(By.ID,'ap_email')

#locator Conditions of use link
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#locator click on the ^ sign
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-expand']").click()
sleep(4)

#Privacy Notice
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")


#Locator Need Help link
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")

#Locator Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#Locator Other issues with Sign-In link
driver.find_element(By.ID,'ap-other-signin-issues-link')

#Locator Create your Amazon account button
driver.find_element(By.XPATH,"//a[@class='a-button-text']")



print("Test Passed")
driver.quit()

