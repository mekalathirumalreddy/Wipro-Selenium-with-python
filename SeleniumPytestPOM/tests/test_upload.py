import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_keyboard:
    def test_keyboard(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)

        # Upload file
        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")
        browse.send_keys(
            r"C:\Users\thiru\OneDrive\Pictures\Screenshots\Screenshot 2026-02-20 215813.png"
        )

        time.sleep(2)

        # Click Upload
        upload = driver.find_element(By.XPATH, "//input[@id='file-submit']")
        upload.click()

        time.sleep(2)

        # Validate upload
        fileupload = driver.find_element(By.XPATH, "//h3")
        assert fileupload.text == "File Uploaded!"

        time.sleep(4)
        driver.quit()