class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"
    # just click actions don't need to insert text like username and password
    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        # other stumped part:  spelling error: find_element_by_link_test > text!
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()
