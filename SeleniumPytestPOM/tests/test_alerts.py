import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Test_Alerts:
    def test_alerts(self):
        options = Options()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # -------- JS Alert --------
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        alert = driver.switch_to.alert
        print("JS Alert text:", alert.text)
        alert.accept()

        # -------- JS Confirm --------
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alert = driver.switch_to.alert
        print("JS Confirm text:", alert.text)
        alert.dismiss()

        # -------- JS Prompt --------
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = driver.switch_to.alert
        print("JS Prompt text:", alert.text)
        alert.send_keys("test hello")
        alert.accept()

        time.sleep(2)
        driver.quit()