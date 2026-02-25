'''
selenium features
1.open source tool
2.web based apps automation
3.cross browser testing - chrome,ff,edge,safari
4.multilanguage support - java ,c#,python,ruby,java script
5.Os supports-windows,linux,mac
'''
#create a fixture for invoke chrome and close the chrome browser

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#create a fixture for invoke chrome browser
@pytest.fixture(scope="function")
def setup(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    #driver set locally is passed to request at class level
    #so that drive is avaliable for other testcases in test folders
    request.cls.driver = driver
    yield
    driver.quit()

