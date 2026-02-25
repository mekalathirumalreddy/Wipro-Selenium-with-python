#check the title of the web page

import pytest
import pages.login_page import loginPage
@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_title(self):
        print(self.driver.title)
        assert "OrangeHRM" in self.driver.title

    def test_valid_login(self,driver):

    def test_invalid_login(self.driver):


#//input[@placeholder='Username']
#//input[@placeholder='Password']
#//button[@type='submit']