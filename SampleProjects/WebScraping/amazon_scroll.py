from selenium import webdriver
import time

scroll_pause_time = 7

driver = webdriver.Firefox()
driver.get("https://www.amazon.com/hz/wishlist/ls/1D7C42EMM4RMP?ref_=wl_share")

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0 ,document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

try:
    parent_class = driver.find_element_by_id("item-page-wrapper")
    item_names = parent_class.find_elements_by_class_name("a-column")
    item_sales = parent_class.find_elements_by_class_name("itemPriceDrop")
    if item_sales and item_names == True:
        for names in item_names:
            print (names.text)

finally:
    driver.close()
