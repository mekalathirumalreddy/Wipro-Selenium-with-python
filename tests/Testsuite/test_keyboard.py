import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Test_keyboard:
    def test_keyboard(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(2)

        actions = ActionChains(driver)

        # Email field
        email = driver.find_element(By.XPATH, "//input[@name='email']")
        email.click()

        # Type HELLO using SHIFT
        actions.key_down(Keys.SHIFT)\
               .send_keys("hello")\
               .key_up(Keys.SHIFT)\
               .perform()

        time.sleep(1)

        # CTRL + A (Select All)
        actions.key_down(Keys.CONTROL)\
               .send_keys("a")\
               .key_up(Keys.CONTROL)\
               .perform()

        # CTRL + C (Copy)
        actions.key_down(Keys.CONTROL)\
               .send_keys("c")\
               .key_up(Keys.CONTROL)\
               .perform()

        time.sleep(1)

        # Password field (use stable locator)
        password = driver.find_element(By.XPATH, "//input[@name='pass']")
        password.click()

        # CTRL + V (Paste)
        actions.key_down(Keys.CONTROL)\
               .send_keys("v")\
               .key_up(Keys.CONTROL)\
               .perform()

        time.sleep(4)
        driver.quit()