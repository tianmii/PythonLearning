# screenshots
# doesn't work for websites that scroll... stitch method??
from selenium import webdriver
import sys
sys.path.extend(["C:\\Users\\tianm\\Selenium\\"])


browser = webdriver.Chrome()
browser.set_window_size(1366, 1728)
browser.get('https://www.ikea.com/ext/us/under-10-deals/')
browser.save_screenshot('screenie.png')
browser.quit()

# -----------
# driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.CHROME.copy())
# driver.get("http://www.google.com")
# driver.get_screenshot_as_file('/Screenshots/google.png')
