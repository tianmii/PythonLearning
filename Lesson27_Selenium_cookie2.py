from selenium import webdriver
import sys

from selenium.webdriver.chrome.options import Options

sys.path.extend(["C:\\Users\\tianm\\Selenium\\"])

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("www.google.com")

