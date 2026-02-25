import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_MultiSelectRadio:
    def test_multiradio(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()
        driver.get("https://testautomationpractice.blogspot.com/")

        # find all checkboxes
        checkbox_list = driver.find_elements(By.XPATH, "//label[@class='form-check-label']")
        count = len(checkbox_list)
        print("Total checkboxes:", count)

        # iterate and click each checkbox
        for checkbox in checkbox_list:
            time.sleep(1)
            checkbox.click()

        # close current browser window
        driver.close()