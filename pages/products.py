from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        #locators
    add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    #adding to cart
    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()
    #adding to cart
    def click_cart(self):
        self.driver.find_element(*self.cart_icon).click()