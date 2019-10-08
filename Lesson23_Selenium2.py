from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# need to import this path
# the first selenium we extended a list, but since we're
# only adding one string "C:\\Users...etc", append is more
# appropriate
import sys
sys.path.append("C:\\Users\\tianm\\Selenium\\")

# Create new instance of Chrome driver
driver = webdriver.Chrome()

# go to google home page
driver.get("http://www.google.com")
print(driver.title)

# find the element that's the name attribute is q (google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("balinese cats")

# submit the form
inputElement.submit()

try:
    # we have to wait for the page to refresh
    WebDriverWait(driver, 10).until(ec.title_contains("balinese cats"))
    # if you see "balinese cats - Google Search" ya did it
    print(driver.title)
finally:
    driver.quit()

