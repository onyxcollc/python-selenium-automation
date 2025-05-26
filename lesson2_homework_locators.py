from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#creating the driver.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#open the url
driver.get('amazon.com')

#locators:
#Amazon logo
driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")

#Email field
driver.find_element(By.ID,"ap_email_login")

#Continue button
driver.find_element(By.XPATH,"//input[@aria-labelledby='continue-announce']")

#Conditions of the use link
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")

#Privacy Notice
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")

#Forgot your password link, Element not there

#Other issues with Sign-In link, Element not there

#Create your Amazon account button, Element not there

