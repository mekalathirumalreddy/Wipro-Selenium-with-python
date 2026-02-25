import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test_MultiSelectRadio:
    def test_multiradio(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        wait = WebDriverWait(driver, 15)

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Login
        wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Wait for dashboard
        wait.until(EC.url_contains("dashboard"))

        # Navigate to employee list
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

        # Wait until checkboxes load
        checkboxes = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//span[contains(@class,'oxd-checkbox-input')]")
            )
        )

        print("Total checkboxes:", len(checkboxes))

        for checkbox in checkboxes:
            driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", checkbox)

        driver.quit()

