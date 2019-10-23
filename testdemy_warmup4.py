"""
Built in  Modules: Importing other pieces of code
Word of advice, dont write from selenium import webdriver
at the top of each function if it's in the same .py file
1. Define all functions
2. Call functions at the very end

"""


from selenium import webdriver
from webbrowser import open

# does not use open function, it's for the bottom two
def youtube():
    driver = webdriver.Chrome()
    driver.get("http://youtube.com")
    driver.close()

# ".open()" is a method or function within a class
# webbrowser.open("http://youtube.com")

def open_ikea():
    # instead of webbrowser.open(), use open()
    open("http://www.ikea.com")

# instead of writing a ton of methods for each individual website
# write a method function and pass the argument "site"

def open_websites(site):
    return open(site)




youtube()

open_ikea()

open_websites("http://legionofhonor.famsf.org")
open_websites("http://deyoung.famsf.org")
open_websites("http://sfmoma.org")
open_websites("http://waltdisney.org")
