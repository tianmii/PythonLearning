from selenium import webdriver
import datetime


def calendar_date_time():
    print(f"{datetime.datetime.now():Today's LampsPlus Sale date is %b %d, %Y}")

# driver.get("https://www.lampsplus.com/products/possini-euro-stride-6-light-bullet-tree-floor-lamp__72v54.html")
# driver.get("https://www.lampsplus.com/products/aaron-aged-brass-3-light-floor-lamp__1k778.html")
def sale_check(url):
    driver = webdriver.Chrome()
    # Gabe: .get() could throw an exception, in which case you'd
    # probably want to close()/quit(), right?
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
    finally:
        driver.close()
        driver.quit()
        print("Test Completed")

# @classmethod
# def tearDownClass(cls):
#     cls.driver.close()
#     cls.driver.quit()
#     print("Test Completed")

calendar_date_time()
sale_check("https://www.lampsplus.com/products/possini-euro-stride-6-light-bullet-tree-floor-lamp__72v54.html")
sale_check("https://www.lampsplus.com/products/aaron-aged-brass-3-light-floor-lamp__1k778.html")
sale_check("https://www.lampsplus.com/products/ellery-brushed-nickel-tree-torchiere-3-light-floor-lamp__1y326.html")

