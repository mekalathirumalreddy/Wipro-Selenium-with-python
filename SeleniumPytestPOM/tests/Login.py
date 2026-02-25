import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

time.sleep(4)

# enter username
username = driver.find_element(By.NAME, "username")
username.send_keys("admin")

# enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

time.sleep(2)

# click login button
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
login_btn.click()

time.sleep(5)

driver.quit()