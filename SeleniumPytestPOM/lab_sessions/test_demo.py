import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test_DemoWebShop:

    def test_login_and_add_to_cart(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        wait = WebDriverWait(driver, 10)

        driver.get("https://demowebshop.tricentis.com/login")
        driver.maximize_window()

        # Login
        wait.until(EC.visibility_of_element_located((By.ID, "Email"))).send_keys("vrun@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("Var@95135785")
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        # Add gift card to cart
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Add to cart']"))).click()

        # Fill gift card details
        wait.until(EC.visibility_of_element_located((By.ID, "giftcard_2_RecipientName"))).send_keys("Varun")

        driver.find_element(By.ID, "giftcard_2_RecipientEmail").send_keys("vrun@gmail.com")

        driver.find_element(By.ID, "add-to-cart-button-2").click()

        time.sleep(3)
        driver.quit()