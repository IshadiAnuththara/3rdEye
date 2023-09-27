from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities import test_utils
from utilities.test_utils import sleep, SHORT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def send_keys_to_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.send_keys(text)

    def find_element(self, locator_name, locator_value):
        return self.get_element(locator_name, locator_value)

    def clear_fields(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.clear()

    def retrieve_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def perform_click_and_image_upload(self, locator_name, locator_value, image_path):
        self.click_element(locator_name, locator_value)
        test_utils.upload_image(image_path)

    def perform_click_and_video_upload(self, locator_name, locator_value, video_path):
        self.click_element(locator_name, locator_value)
        test_utils.upload_video(video_path)

    def send_keys_and_tab(self, locator_name, locator_value):
        element = self.driver.find_element(locator_name, locator_value)
        element.send_keys(Keys.ARROW_RIGHT)

    def get_element_attribute(self, locator_name, locator_value, attribute_name):
        element = self.get_element(locator_name, locator_value)
        return element.get_attribute(attribute_name)

    def set_element_value_with_tab(self, locator_name, locator_value, value):
        element = self.get_element(locator_name, locator_value)
        element.send_keys(Keys.TAB)
        sleep(3)
        element.send_keys(value)

    def set_date(self, locator_name, locator_value, date):
        self.send_keys_to_element(date, locator_name, locator_value)
        sleep(SHORT_WAIT)
        self.send_keys_and_tab(locator_name, locator_value)

    def quit(self):
        self.driver.quit()
