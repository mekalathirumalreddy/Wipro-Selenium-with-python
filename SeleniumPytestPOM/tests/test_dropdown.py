from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# locate dropdown
dropdown_element = driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")

# create Select object
dropdown = Select(dropdown_element)

# select by visible text
dropdown.select_by_visible_text("Option1")
time.sleep(2)

# select by value (lowercase!)
dropdown.select_by_value("option2")
time.sleep(2)

# select by index
dropdown.select_by_index(3)
time.sleep(2)

driver.quit()