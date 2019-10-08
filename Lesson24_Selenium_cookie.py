from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import sys

sys.path.append("C:\\Users\\tianm\\Selenium\\")

# Create new instance of Chrome driver
driver = webdriver.Chrome()

driver.get("http://www.amazon.com")
driver.add_cookie({
    'name': 'key',
    'value': 'value',
    'path': '/'
})

for cookie in driver.get_cookies():
    print(f"{cookie['name']} => {cookie['value']}")

