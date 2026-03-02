import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


DOWNLOAD_DIR = r"C:\Users\thiru\Downloads"


class Test_download:
    def test_dw(self):

        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": DOWNLOAD_DIR,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        # Click file
        file_name = "alert.jpeg"
        driver.find_element(By.LINK_TEXT, file_name).click()

        time.sleep(5)

        # Verify file download
        file_path = os.path.join(DOWNLOAD_DIR, file_name)
        assert os.path.exists(file_path), "File not downloaded"

        driver.quit()