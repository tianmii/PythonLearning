from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("https://www.lampsplus.com/products/aaron-aged-brass-3-light-floor-lamp__1k778.html")
driver.get("https://www.lampsplus.com/products/possini-euro-stride-6-light-bullet-tree-floor-lamp__72v54.html")
html_list = driver.find_element_by_id("priceAdditionalSave")
items = html_list.find_elements_by_xpath("//*[@id='priceAdditionalSave']")
for item in items:
    text = item.text
    print(text)
print("Test Completed")
