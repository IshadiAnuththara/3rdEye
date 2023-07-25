import time
from selenium.webdriver.common.by import By


class EyeDonationPage:
    hyperlink_eyeDonation_xpath = "//a[normalize-space()='Eye Donations']"
    input_search_xpath = "//input[@placeholder='Search name']"
    span_search_xpath = "//span[@class='anticon anticon-search']"
    span_refresh_xpath = "(//button[@class='ant-btn d-flex align-items-center " \
                         "p-0 justify-content-center ng-star-inserted'])[1]"
    button_viewEyeDonation_xpath = "(//button[@class='ant-btn btn ant-btn-icon-only ng-star-inserted'])[1]"
    button_close_xpath = "//button[@aria-label='Close']"
    button_delete_xpath = "//tbody/tr[1]/td[4]/nz-space[1]/div[2]/button[1]"
    span_ok_xpath = "//span[normalize-space()='OK']"

    def __init__(self, driver):
        self.driver = driver

    def clickEyeDonation(self):
        self.driver.find_element(By.XPATH, self.hyperlink_eyeDonation_xpath).click()

    def setSearch(self, name):
        self.driver.find_element(By.XPATH, self.input_search_xpath).send_keys(name)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.span_search_xpath).click()

    def clickRefresh(self):
        self.driver.find_element(By.XPATH, self.span_refresh_xpath).click()

    def clickViewEyeDonation(self):
        self.driver.find_element(By.XPATH, self.button_viewEyeDonation_xpath).click()

    def clickClose(self):
        self.driver.find_element(By.XPATH, self.button_close_xpath).click()

    def clickDelete(self):
        self.driver.find_element(By.XPATH, self.button_delete_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.span_ok_xpath).click()
