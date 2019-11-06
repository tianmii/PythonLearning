class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        # naming convention is important, so when others read it, it is detailed
        # advantage of Page Object Model is that many tests might use the variable
        # txtUsername, but you only need to change it once in all tests if you need to
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        # line up the ids so it's readable
        self.login_button_id     = "btnLogin"

    # create action methods
    def enter_username(self, username):
        # good practice to clear text objects before sending keys
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        # STUMPED PART: PARAMETER IN DEF USERNAME AND PASSWORD WERE GREYED OUT
        # send_keys("username") is incorrect!
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    # no input needed like username and password, no need for other parameters
    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
