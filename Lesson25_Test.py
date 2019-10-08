# Implicit and explicit wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import sys
sys.path.extend(["C:\\Users\\tianm\\Selenium\\"])

c = webdriver.Chrome()
c.get("https://www.ikea.com/ext/us/new-lower-price/?itm_campaign=OWFEHP&itm_element=HeroSlider2&itm_content"
      "=New_Lower_Price")

try:
    element = WebDriverWait(c, .5).until(ec.presence_of_element_located((By.ID, "ourLovelyApp")))
finally:
    c.quit()
