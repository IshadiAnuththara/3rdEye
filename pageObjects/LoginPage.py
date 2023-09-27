from locators.common_locators import CommonLocators
from locators.login_locators import LoginPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()
        self.locator = CommonLocators()

    def set_username(self, username):
        self.send_keys_to_element(username, "input_username_xpath", self.locators.input_username_xpath)

    def set_password(self, password):
        self.send_keys_to_element(password, "input_password_xpath", self.locators.input_password_xpath)

    def set_invalid_username(self, username):
        self.send_keys_to_element(username, "input_username_xpath", self.locators.input_username_xpath)

    def set_invalid_password(self, password):
        self.send_keys_to_element(password, "input_password_xpath", self.locators.input_password_xpath)

    def click_login(self):
        self.click_element("button_login_xpath", self.locators.button_login_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def clear_username(self):
        self.clear_fields("input_username_xpath", self.locators.input_username_xpath)

    def clear_password(self):
        self.clear_fields("input_password_xpath", self.locators.input_password_xpath)

    def login_to_application(self, username, password):
        self.set_username(username)
        sleep(SHORT_WAIT)
        self.set_password(password)
        sleep(SHORT_WAIT)
        self.click_login()

    def login_with_valid_username_and_invalid_password(self, email_address_text, password_text):
        self.set_username(email_address_text)
        self.set_invalid_password(password_text)
        return self.click_login()

    def login_with_invalid_username_and_valid_password(self, email_address_text, password_text):
        self.set_invalid_username(email_address_text)
        self.set_password(password_text)
        return self.click_login()

    def login_with_invalid_username_and_invalid_password(self, email_address_text, password_text):
        self.set_invalid_username(email_address_text)
        self.set_invalid_password(password_text)
        return self.click_login()

    def login_without_enter_username_password(self):
        self.clear_username()
        self.clear_password()
        return self.click_login()

    
