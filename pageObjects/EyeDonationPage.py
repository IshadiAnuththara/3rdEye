from locators.common_locators import CommonLocators
from locators.eye_donation_locators import EyeDonationPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class EyeDonationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = EyeDonationPageLocators()
        self.locator = CommonLocators()

    def click_eye_donation(self):
        self.click_element("hyperlink_eye_donation_xpath", self.locators.hyperlink_eye_donation_xpath)

    def set_search(self, name):
        self.send_keys_to_element(name, "input_search_xpath", self.locators.input_search_xpath)

    def click_search(self):
        self.click_element("span_search_xpath", self.locators.span_search_xpath)

    def click_refresh(self):
        self.click_element("span_refresh_xpath", self.locators.span_refresh_xpath)

    def click_view_eye_donation(self):
        self.click_element("button_view_eye_donation_xpath", self.locators.button_view_eye_donation_xpath)

    def click_close(self):
        self.click_element("button_close_xpath", self.locators.button_close_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_ok_xpath", self.locators.span_ok_xpath)

    def search_eye_donation(self, name):
        self.set_search(name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
