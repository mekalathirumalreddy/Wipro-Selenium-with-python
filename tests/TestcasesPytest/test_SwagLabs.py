import time

from pages.swagLabs_login import LoginPage
from pages.products import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from utilities.logger import get_logger
from utilities.Excel_utils import get_excel_data

logger = get_logger()
test_data = get_excel_data("C:/Users/thiru/PycharmProjects/SeleniumPytestPOM/testdata/login_data.xlsx", "Sheet1")


class TestSwagLabsE2E:

    def test_end_to_end_flow(self, driver):
        logger.info("Opening application")
        driver.get("https://www.saucedemo.com/")
        time.sleep(4)
        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")
        time.sleep(4)

        product = ProductPage(driver)
        time.sleep(2)
        product.add_to_cart()
        time.sleep(2)
        product.click_cart()
        time.sleep(3)

        cart = CartPage(driver)
        cart.click_checkout()
        time.sleep(3)
        checkout = CheckoutPage(driver)
        checkout.enter_details("Thiru", "Reddy", "500001")
        time.sleep(3)
        overview = OverviewPage(driver)
        overview.finish_order()
        time.sleep(4)
        assert "Thank you for your order!" in driver.page_source
