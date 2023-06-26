import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver

from pageObjects.EyeDonationPage import EyeDonationPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchEyeDonation:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchEyeDonation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()

        # Access Eye Donation

        time.sleep(4)
        self.ed = EyeDonationPage(self.driver)
        self.ed.clickEyeDonation()
        time.sleep(3)

        # Search Eye donations by name

        self.ed.setSearch("kavindu")
        time.sleep(3)
        self.ed.clickSearch()
        time.sleep(3)
        self.ed.clickRefresh()

        time.sleep(5)
        self.driver.close()
