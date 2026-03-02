import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_browser_commands:
    def test_browser_commands(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://trytestingthis.netlify.app/")
        driver.maximize_window()
        time.sleep(2)

        # Browser interactions
        print("Title:", driver.title)
        print("URL:", driver.current_url)


        # Navigation commands
        driver.back()
        time.sleep(2)

        driver.forward()
        time.sleep(2)

        driver.refresh()
        time.sleep(2)

        driver.quit()