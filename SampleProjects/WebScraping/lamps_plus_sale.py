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
        additional_save = html_list.find_elements_by_xpath("//*[@id='priceAdditionalSave']")
        for item in additional_save:
            savings_text = item.text
            print(f"{savings_text}\n")
    except:
        print("There are no sales today.\n")
    # finally:
    #     driver.quit()
    #     driver.close()



# calendar_date_time()
# sale_check("https://www.lampsplus.com/products/possini-euro-stride-6-light-bullet-tree-floor-lamp__72v54.html")
sale_check("https://www.lampsplus.com/products/aaron-aged-brass-3-light-floor-lamp__1k778.html")
sale_check("https://www.lampsplus.com/products/ellery-brushed-nickel-tree-torchiere-3-light-floor-lamp__1y326.html")

