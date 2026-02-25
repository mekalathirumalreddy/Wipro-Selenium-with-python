from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_Waits:
    def test_waits(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()
        driver.get("https://demoqa.com/radio-button")

        # ---------- Explicit Wait ----------
        wait = WebDriverWait(driver, 10)

        radio_btn = wait.until(
            lambda driver: driver.find_element(By.ID, "yesRadio")
        )

        assert radio_btn.is_displayed()

        # ---------- Custom / Fluent Wait ----------
        errors = (NoSuchElementException, ElementNotInteractableException)

        wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=errors
        )

        wait.until(lambda driver: radio_btn.is_enabled())
        radio_btn.click()

        driver.quit()