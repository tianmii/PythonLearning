from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.find_element_by_id("hplogo").click()

print("Test Completed")