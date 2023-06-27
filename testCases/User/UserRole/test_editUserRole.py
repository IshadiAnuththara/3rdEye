import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_EditUserRole:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_editUserRole(self, setup):
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
        time.sleep(3)

        # Edit User Role

        self.ur.clickEdit()
        time.sleep(3)
        self.ur.editRoleName("Testing")
        time.sleep(3)
        self.ur.removePermission_UserManagement()
        time.sleep(3)
        self.ur.removePermission_Recipies()
        time.sleep(3)
        self.ur.clickSave()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text
        print(self.msg)
        if 'Successfully Updated.' in self.msg:
            assert True
            self.logger.info("********* Edit User Role Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_editUserRole_scr.png")  # Screenshot
            self.logger.error("********* Edit User Role Test Failed ************")
            assert False
        self.driver.close()


