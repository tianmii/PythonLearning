from selenium import webdriver
import datetime


def calendar_date_time():
    print(f"{datetime.datetime.now():Today's LampsPlus Sale date is %b %d, %Y}")
def sale_check(url):
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        lamp_name = driver.find_element_by_xpath("//*[@id='h1ProductName']")
        print(lamp_name.text)
        original_price = driver.find_element_by_xpath("//*[@id='lblPrice']")
        print(original_price.text)
        html_list = driver.find_element_by_id("priceAdditionalSave")
        items = html_list.find_elements_by_xpath("//*[@id='priceAdditionalSave']")
        for item in items:
            savings_text = item.text
            print(f"{savings_text}\n")
    except:
        print("There are no sales today.\n")
        driver.close()
    finally:
        driver.quit()
        driver.close()



calendar_date_time()
sale_check("https://www.lampsplus.com/products/possini-euro-stride-6-light-bullet-tree-floor-lamp__72v54.html")
sale_check("https://www.lampsplus.com/products/aaron-aged-brass-3-light-floor-lamp__1k778.html")
sale_check("https://www.lampsplus.com/products/ellery-brushed-nickel-tree-torchiere-3-light-floor-lamp__1y326.html")

























# from selenium import webdriver
# import datetime
# import unittest
#
#
# # 1. Run > Edit Configurations
#
# def calendar_date_time():
#     print(f"{datetime.datetime.now():Today's LampsPlus Sale date is %b %d, %Y}")
#
# # driver.get("https://www.lampsplus.com/products/possini-euro-stride-6-light-bullet-tree-floor-lamp__72v54.html")
# # driver.get("https://www.lampsplus.com/products/aaron-aged-brass-3-light-floor-lamp__1k778.html")
#
# def setUpClass(cls):
#     cls.driver = webdriver.Chrome()
#     cls.driver.implicitly_wait(10)
#     cls.driver.maximize_window()
# def sale_check(url):
#
#     # Gabe: .get() could throw an exception, in which case you'd
#     # probably want to close()/quit(), right?
#     driver = webdriver
#     try:
#         lamp_name = driver.find_element_by_xpath("//*[@id='h1ProductName']")
#         print(lamp_name.text)
#         original_price = driver.find_element_by_xpath("//*[@id='lblPrice']")
#         print(original_price.text)
#         # html_list = driver.find_element_by_id("priceAdditionalSave")
#         items = driver.find_elements_by_xpath("//*[@id='priceAdditionalSave']")
#         for item in items:
#             savings_text = item.text
#             print(f"{savings_text}\n")
#     except:
#         print("There are no sales today.\n")
#     finally:
#         driver.close()
#         driver.quit()
#
#     # @classmethod
#     # def tearDownClass(cls):
#     #     cls.driver.close()
#     #     cls.driver.quit()
#     #     print("Test Completed")
#
# calendar_date_time()
# sale_check("https://www.lampsplus.com/products/possini-euro-stride-6-light-bullet-tree-floor-lamp__72v54.html")
# sale_check("https://www.lampsplus.com/products/aaron-aged-brass-3-light-floor-lamp__1k778.html")
# sale_check("https://www.lampsplus.com/products/ellery-brushed-nickel-tree-torchiere-3-light-floor-lamp__1y326.html")
#
