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
class Test_WH:
    def test_wh(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://jqueryui.com/datepicker/")
        time.sleep(2)
        driver.implicitly_wait(10)
        #frame = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
        driver.switch_to.frame(0)

        datepicker=driver.find_element(By.XPATH,"//input[@id='datepicker']")
        datepicker.click()
        time.sleep(3)
        driver.close()