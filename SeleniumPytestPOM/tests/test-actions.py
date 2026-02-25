import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class Test_Actions:
    def test_actions(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        time.sleep(2)

        actions = ActionChains(driver)

        # Double click on Best Sellers
        bestsellers = driver.find_element(
            By.XPATH, "//a[contains(@href,'/gp/bestsellers')]"
        )
        actions.double_click(bestsellers).perform()
        time.sleep(2)

        driver.back()
        time.sleep(2)

        # Right click on Mobiles
        mobiles = driver.find_element(By.XPATH, "//a[normalize-space()='Mobiles']")
        actions.context_click(mobiles).perform()
        time.sleep(2)

        #move element
        primes = driver.find_element(By.XPATH,"//span[normalize-space()='prime']")
        actions.move_to_element(primes).perform()

        #click and hold
        fresh =dr

        driver.quit()