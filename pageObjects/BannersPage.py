from locators.banners_locators import BannersPageLocators
from locators.common_locators import CommonLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class BannersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = BannersPageLocators()
        self.locator = CommonLocators()

    def click_banners(self):
        self.click_element("hyperlink_banners_xpath", self.locators.hyperlink_banners_xpath)

    def click_add_banner(self):
        self.click_element("span_add_banner_xpath", self.locators.span_add_banner_xpath)

    def click_upload(self):
        self.click_element("span_upload_xpath", self.locators.span_upload_xpath)

    def click_choose_image(self):
        self.perform_click_and_image_upload("span_choose_image_xpath", self.locators.span_choose_image_xpath,
                                            self.locators.upload_image)

    def click_add(self):
        self.click_element("span_add_xpath", self.locators.span_add_xpath)

    def click_save(self):
        self.click_element("span_save_xpath", self.locators.span_save_xpath)

    def click_edit(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)

    def upload_new_banner(self):
        self.perform_click_and_image_upload("span_choose_image_xpath", self.locators.span_choose_image_xpath,
                                            self.locators.upload_banner)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_ok_xpath", self.locators.span_ok_xpath)

    def click_checkbox(self):
        self.click_element("span_checkbox_xpath", self.locators.span_checkbox_xpath)

    def click_close(self):
        self.click_element("button_close_xpath", self.locators.button_close_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def add_new_banner(self):
        self.click_add_banner()
        sleep(SHORT_WAIT)
        self.click_upload()
        sleep(SHORT_WAIT)
        self.click_choose_image()
        sleep(SHORT_WAIT)
        self.click_add()
        sleep(SHORT_WAIT)
        self.click_save()

    def close_banners(self):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.click_close()
        sleep(SHORT_WAIT)
        self.driver.switch_to.alert.accept()

    def edit_banners(self):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.click_upload()
        sleep(SHORT_WAIT)
        self.click_choose_image()
        sleep(SHORT_WAIT)
        self.click_add()
        sleep(SHORT_WAIT)
        self.click_save()
