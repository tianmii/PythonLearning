# screenshots
# doesn't work for websites that scroll... stitch method??
from selenium import webdriver
import sys

sys.path.extend(["C:\\Users\\tianm\\Selenium\\"])


def save_screenshot(browser: webdriver.Chrome(), path: str = 'tmp/screenshot.png'):
    browser.get('https://www.ikea.com/ext/us/under-10-deals/')
    original_size = browser.get_window_size()
    required_width = browser.execute_script('return document.body.parentNode.scrollWidth')
    required_height = browser.execute_script('return document.body.parentNode.scrollHeight')
    browser.set_window_size(required_width, required_height)
    browser.find_element_by_tag_name('body').screenshot(path)
    browser.set_window_size(original_size['width'], original_size['height'])


save_screenshot()

# height = browser.execute_script("return document.documentElement.scrollHeight")
# browser.execute_script(f"window.scrollTo(0, {str(height)})")
# browser.find_element_by_tag_name('body').screenshot('web_screenshot.png')
# browser.quit()
