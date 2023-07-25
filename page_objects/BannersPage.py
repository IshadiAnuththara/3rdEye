import time

import pyautogui
from selenium.webdriver.common.by import By


class BannersPage:
    hyperlink_banners_xpath = "//a[normalize-space()='Banners']"
    span_add_banner_xpath = "//span[normalize-space()='Add banner']"
    span_upload_xpath = "//span[normalize-space()='+Upload']"
    span_choose_image_xpath = "//span[normalize-space()='Choose new image']"
    span_add_xpath = "//span[normalize-space()='Add']"
    span_save_xpath = "//span[normalize-space()='Save']"
    button_edit_xpath = "/html/body/blind-app-root/blind-app-layout/nz-layout/nz-layout/nz-content/div[" \
                        "2]/blind-app-banner/div/div/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table" \
                        "/tbody/tr[1]/td[3]/button[1]"
    button_delete_xpath = "/html/body/blind-app-root/blind-app-layout/nz-layout/nz-layout/nz-content/div[" \
                          "2]/blind-app-banner/div/div/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table" \
                          "/tbody/tr[1]/td[3]/button[2]"
    span_ok_xpath = "//span[normalize-space()='OK']"
    span_checkbox_xpath = "//span[@class='ant-checkbox']"
    button_close_xpath = "(//button[@type='button'])[4]"

    def __init__(self, driver):
        self.driver = driver

    def click_banners(self):
        self.driver.find_element(By.XPATH, self.hyperlink_banners_xpath).click()

    def click_add_banner(self):
        self.driver.find_element(By.XPATH, self.span_add_banner_xpath).click()

    def click_upload(self):
        self.driver.find_element(By.XPATH, self.span_upload_xpath).click()

    def click_choose_image(self):
        self.driver.find_element(By.XPATH, self.span_choose_image_xpath).click()
        time.sleep(3)
        # Set the file path of the AutoIT script
        autoit_script = "C:\\Users\\Ishadi\\Pictures\\3rd eye\\testBanner_01.jpg"
        time.sleep(1)
        pyautogui.typewrite(autoit_script)
        pyautogui.press("enter")

    def click_add(self):
        self.driver.find_element(By.XPATH, self.span_add_xpath).click()

    def click_save(self):
        self.driver.find_element(By.XPATH, self.span_save_xpath).click()

    def click_edit(self):
        self.driver.find_element(By.XPATH, self.button_edit_xpath).click()

    def upload_new_banner(self):
        self.driver.find_element(By.XPATH, self.span_choose_image_xpath).click()
        time.sleep(3)
        # Set the file path of the AutoIT script
        autoit_script = "C:\\Users\\Ishadi\\Pictures\\3rd eye\\test_banner_02.jpg"
        time.sleep(1)
        pyautogui.typewrite(autoit_script)
        pyautogui.press("enter")

    def click_delete(self):
        self.driver.find_element(By.XPATH, self.button_delete_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.span_ok_xpath).click()

    def click_checkbox(self):
        self.driver.find_element(By.XPATH, self.span_checkbox_xpath).click()

    def click_close(self):
        self.driver.find_element(By.XPATH, self.button_close_xpath).click()
