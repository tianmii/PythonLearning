from selenium import webdriver

def sale_checker(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        # name
        lamp_name = driver.find_element_by_xpath("//*[@id='h1ProductName']")
        print(lamp_name.text)
        # price
        original_price = driver.find_element_by_xpath("//*[@id='lblPrice']")
        print(original_price.text)
        # new savings
        html_list = driver.find_element_by_id("priceAdditionalSave")
        additional_savings = html_list.find_elements_by_xpath("//*[@id='priceAdditionalSave']")
        for item in additional_savings:
            savings_text = item.text
            print(f"{savings_text}\n")
    except:
        print("There is no sale today.\n")
    finally:
        driver.close()
        print("Test complete.")


sale_checker("https://www.lampsplus.com/products/aaron-aged-brass-3-light-floor-lamp__1k778.html")
sale_checker("https://www.lampsplus.com/products/possini-euro-stride-6-light-bullet-tree-floor-lamp__72v54.html")
sale_checker("https://www.lampsplus.com/products/ellery-brushed-nickel-tree-torchiere-3-light-floor-lamp__1y326.html")

