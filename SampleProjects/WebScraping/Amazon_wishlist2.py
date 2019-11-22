from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/hz/wishlist/ls/1D7C42EMM4RMP?ref_=wl_share")

while True:
    try:
        item_sale = driver.find_elements_by_class_name("itemPriceDrop")
        item_name = driver.find_elements_by_class_name("a-list-item")

        for sale in item_sale:
            print(sale.text)



    finally:

        time.sleep(2)
        print("Test Complete")
        driver.close()


