from multiprocessing.resource_tracker import register

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver =webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
time.sleep(3)

register = driver.find_element(By.XPATH,"//input[@value='Register']")
register.click()

gender=driver.find_element(By.XPATH,"//input[@id='gender-male']")
gender.click()

first_name=driver.find_element(By.XPATH,"//input[@id='FirstName']")
first_name.send_keys("varun")

last_name =driver.find_element(By.XPATH,"//input[@id='LastName']")
last_name.send_keys("Varun")

email=driver.find_element(By.XPATH,"//input[@id='Email']")
email.send_keys("vrun@gmail.com")

password =driver.find_element(By.XPATH,"//input[@id='Password']")
password.send_keys("Var@95135785")

confirm_password=driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']")
confirm_password.send_keys("Var@95135785")
time.sleep(4)

register1=driver.find_element(By.XPATH,"//input[@id='register-button']")
register1.click()
time.sleep(3)

continue1=driver.find_element(By.XPATH,"//input[@value='Continue']")
continue1.click()

driver.close()