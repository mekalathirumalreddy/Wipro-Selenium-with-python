from selenium.webdriver.common.by import By


class OverviewPage:

    def __init__(self, driver):
        self.driver = driver

    finish_btn = (By.ID, "finish")

    def finish_order(self):
        self.driver.find_element(*self.finish_btn).click()