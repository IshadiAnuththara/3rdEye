import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchUser:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchUser(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(2)

        # Access User

        self.userManagement = UserPage(self.driver)
        self.userManagement.clickUser()
        time.sleep(3)

        # Access User Management

        self.userManagement.clickUserManagement()
        time.sleep(3)

        # Search User

        self.userManagement.setSearch("superAdmin")
        time.sleep(2)
        self.userManagement.clickSearch()
        time.sleep(3)
        self.userManagement.clickRefresh()
        time.sleep(4)
        self.driver.close()

