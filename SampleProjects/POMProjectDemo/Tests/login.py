from selenium import webdriver
# import sys
#
# sys.path.extend(["C:\\Users\\tianm\\Selenium\\"])
import time
import unittest
from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):
    # class functions need the annotation "@classmethod"
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        # inspect each element of this open source login
        # inspect and find id name if possible for username,
        # password, and login button text box
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

        # will only execute once all the tests are completed to close browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


"""
        # action is send_keys after finding element
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        # no properties/id for logout, use the link
        self.driver.find_element_by_link_text("Logout").click()
"""
