from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_WebTable:
    def test_table(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/tables")
        time.sleep(2)

        # Fetch all rows
        rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
        print("Rows:")
        for row in rows:
            print(row.text)

        # Fetch all columns from first row
        columns = driver.find_elements(
            By.XPATH, "//table[@id='table1']/tbody/tr[1]/td"
        )
        print("\nColumns:")
        for col in columns:
            print(col.text)

        # Fetch single cell value (Row 3, Column 4)
        cell_data = driver.find_element(
            By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[4]"
        )

        assert "$100.00" in cell_data.text

        driver.quit()