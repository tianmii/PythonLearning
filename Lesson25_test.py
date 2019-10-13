# screenshots
# doesn't work for websites that scroll... stitch method??
from selenium import webdriver

import sys

sys.path.extend(["C:\\Users\\tianm\\Selenium\\"])

options = webdriver.ChromeOptions()
options.headless = True

browser = webdriver.Chrome()
browser.get('https://www.ikea.com/ext/us/under-10-deals/')

s = lambda x: browser.execute_script('return document.body.parentNode.scroll' + x)
browser.set_window_size(s('Width'), s('Height'))
browser.find_element_by_tag_name('body').screenshot('web_screenshot.png')
browser.quit()
