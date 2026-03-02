from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_site:
    def test_st(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(2)

        # Enter text
        suggestion = driver.find_element(By.ID, "autocomplete")
        suggestion.send_keys("ch")
        time.sleep(2)

        # Fetch all suggestions
        countries = driver.find_elements(
            By.XPATH, "//li[@class='ui-menu-item']/div"
        )

        # Select China
        for country in countries:
            if country.text == "China":
                country.click()
                break

        time.sleep(3)
        driver.quit()