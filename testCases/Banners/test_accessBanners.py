import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.BannersPage import BannersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AccessBanners:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_accessBanners(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(4)

        # Access Banners

        self.banners = BannersPage(self.driver)
        self.banners.clickBanners()
        self.logger.info("********* Access Banners - Test Passed *********")
        time.sleep(5)
        self.driver.close()
