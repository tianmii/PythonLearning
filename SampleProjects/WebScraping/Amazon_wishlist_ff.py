from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.amazon.com/hz/wishlist/ls/1D7C42EMM4RMP?ref_=wl_share")


def popup_time_wait():
    time.sleep(5)


def scroll_time():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0 ,document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def amazon_wishlist():
    try:
        parent_class = driver.find_element_by_id("item-page-wrapper")
        item_names = parent_class.find_elements_by_class_name("a-column")
        # could not link item_sales to item_names in the if statement
        # item_sales = parent_class.find_elements_by_class_name("itemPriceDrop")
        for name in item_names:
            if "price dropped" in name.text.lower():
                print(f"{name.text}\n")
                # print("price dropped" in name.text.lower())
    finally:
        time.sleep(1)
        print("Test Complete")
        driver.close()


popup_time_wait()
scroll_time()
amazon_wishlist()
