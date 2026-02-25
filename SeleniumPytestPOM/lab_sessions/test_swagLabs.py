import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_login:
    def test_web(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        time.sleep(2)

        username = driver.find_element(By.XPATH, "//input[@id='user-name']")
        username.send_keys("standard_user")

        password = driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys("secret_sauce")

        login_btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_btn.click()
        time.sleep(3)

        add_to_cart=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_cart.click()
        time.sleep(3)

        open_cart=driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        open_cart.click()
        time.sleep(3)

        check_out = driver.find_element(By.XPATH,"//button[@id='checkout']")
        check_out.click()
        time.sleep(3)

        first_name = driver.find_element(By.XPATH,"//input[@id='first-name']")
        first_name.send_keys("Varun")

        last_name = driver.find_element(By.XPATH,"//input[@id='last-name']")
        last_name.send_keys("reddy")

        postal_code =driver.find_element(By.XPATH,"//input[@id='postal-code']")
        postal_code.send_keys("50232")
        time.sleep(3)

        continue_o =driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_o.click()
        time.sleep(3)
        finish = driver.find_element(By.XPATH,"//button[@id='finish']")
        finish.click()



        time.sleep(3)
        driver.quit()