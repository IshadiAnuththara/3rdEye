from locators.common_locators import CommonLocators
from locators.logout_locators import LogoutPageLocators
from pageObjects.BasePage import BasePage


class Logout(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LogoutPageLocators()
        self.locator = CommonLocators()

    def set_username(self, username):
        self.send_keys_to_element(username, "input_username_xpath", self.locators.input_username_xpath)

    def set_password(self, password):
        self.send_keys_to_element(password, "input_password_xpath", self.locators.input_password_xpath)

    def click_login(self):
        self.click_element("button_login_xpath", self.locators.button_login_xpath)

    def click_logout(self):
        self.click_element("button_logout_xpath", self.locators.button_logout_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)
