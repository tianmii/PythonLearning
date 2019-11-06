# Google search test

from selenium import webdriver
import sys
sys.path.extend(["C:\\Users\\tianm\\Selenium\\"])
import unittest


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("btnK").click()

    def test_search_lavender(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("lavender")
        self.driver.find_element_by_name("btnK").click()

   
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

