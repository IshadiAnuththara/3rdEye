import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AddUserRole:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addUserRole(self, setup):
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

        self.ur = UserPage(self.driver)
        self.ur.clickUser()
        time.sleep(3)

        # Access User Role

        self.ur.clickUserRole()

        # Add new User Role
        self.ur.clickAddUserRole()
        time.sleep(3)
        self.ur.setRole("Test User")
        time.sleep(3)
        self.ur.clickPermission()
        time.sleep(2)
        self.ur.clickPermission_UserManagement()
        time.sleep(2)
        self.ur.clickPermission_Recipies()
        time.sleep(2)
        self.ur.clickPermission_EyeDonations()
        time.sleep(2)
        self.ur.clickPermission_Banners()
        time.sleep(2)
        self.ur.clickSave()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text
        print(self.msg)
        if 'Successfully Created.' in self.msg:
            assert True
            self.logger.info("********* Add User Role Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addUserRole_scr.png")  # Screenshot
            self.logger.error("********* Add User Role Test Failed ************")
            assert False
        self.driver.close()


