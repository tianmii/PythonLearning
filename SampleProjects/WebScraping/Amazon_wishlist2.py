from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/hz/wishlist/ls/1D7C42EMM4RMP?ref_=wl_share")


try:
    parent_class = driver.find_element_by_id("item-page-wrapper")
    item_names = parent_class.find_elements_by_class_name("a-column")
    item_sales = parent_class.find_elements_by_class_name("itemPriceDrop")
    if item_sales:
        for name in item_names:
            print(f"{name.text}\n")

    # print(parent_class.text)

finally:
    time.sleep(2)
    print("Test Complete")
    driver.close()
# if True:
#     try:
#         # item_sale = driver.find_elements_by_class_name("itemPriceDrop")
#         item_name = driver.find_elements_by_class_name("a-section")
#         for name in item_name:
#             print(name.text)
#         # for sale in item_sale:
#         #     print(sale.text)
#     finally:
#         time.sleep(2)
#         print("Test Complete")
#         driver.close()



# try:
#     urls = driver.find_elements_by_tag_name("a").get_attribute('href')
#     for url in urls:
#         print(url.text)
    # item_sale = driver.find_elements_by_class_name("itemPriceDrop")


    # for sale in item_sale:
    #     print(sale.text)

