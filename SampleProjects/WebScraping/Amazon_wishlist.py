from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/hz/wishlist/ls/1D7C42EMM4RMP?ref_=wl_share")
# current_price = driver.find_element_by_id("itemPrice_I19IH1YAURA6D3")
# print(current_price.text)
# item_names = driver.find_elements_by_xpath("//*[@id='itemName_I3HIELKIL93978']")
# for item in item_names:
#     print(item.text)

try:
    item_price = driver.find_elements_by_class_name("a-list-item")
    for item in item_price:
        print(f"{item.text}\n")




finally:
    time.sleep(2)
    print("Test Complete")
    driver.close()

# price_dropped = driver.find_elements_by_xpath("//*[@id='itemInfo_IXCN0JX27H5HG']")
# print(price_dropped)