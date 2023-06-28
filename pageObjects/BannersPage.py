import time

import pyautogui
from selenium.webdriver.common.by import By


class BannersPage:
    hyperlink_banners_xpath = "//a[normalize-space()='Banners']"
    span_addBanner_xpath = "//span[normalize-space()='Add banner']"
    span_upload_xpath = "//span[normalize-space()='+Upload']"
    span_chooseImage_xpath = "//span[normalize-space()='Choose new image']"
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

    def __init__(self, driver):
        self.driver = driver

    def clickBanners(self):
        self.driver.find_element(By.XPATH, self.hyperlink_banners_xpath).click()

    def clickAddBanner(self):
        self.driver.find_element(By.XPATH, self.span_addBanner_xpath).click()

    def clickUpload(self):
        self.driver.find_element(By.XPATH, self.span_upload_xpath).click()

    def clickChooseImage(self):
        self.driver.find_element(By.XPATH, self.span_chooseImage_xpath).click()
        time.sleep(3)
        # Set the file path of the AutoIT script
        autoit_script = "C:\\Users\\Ishadi\\Pictures\\3rd eye\\testBanner_01.jpg"
        time.sleep(1)
        pyautogui.typewrite(autoit_script)
        pyautogui.press("enter")

    def clickAdd(self):
        self.driver.find_element(By.XPATH, self.span_add_xpath).click()

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.span_save_xpath).click()

    def clickEdit(self):
        self.driver.find_element(By.XPATH, self.button_edit_xpath).click()

    def uploadNewBanner(self):
        self.driver.find_element(By.XPATH, self.span_chooseImage_xpath).click()
        time.sleep(3)
        # Set the file path of the AutoIT script
        autoit_script = "C:\\Users\\Ishadi\\Pictures\\3rd eye\\test_banner_02.jpg"
        time.sleep(1)
        pyautogui.typewrite(autoit_script)
        pyautogui.press("enter")

    def clickDelete(self):
        self.driver.find_element(By.XPATH, self.button_delete_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.span_ok_xpath).click()

    def clickCheckbox(self):
        self.driver.find_element(By.XPATH, self.span_checkbox_xpath).click()