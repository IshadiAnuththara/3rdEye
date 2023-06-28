import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AddMember_Invalid_AddExistingEmail:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addMember(self, setup):
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

        # Add Member

        self.userManagement.clickAddMember()
        time.sleep(2)
        self.userManagement.setUsername("TestUser")
        time.sleep(3)
        self.userManagement.clickGeneratePassword()
        time.sleep(5)
        self.userManagement.setEmail("miwabog446@fitwl.com")
        time.sleep(3)
        self.userManagement.setFirstName("Brielle")
        time.sleep(3)
        self.userManagement.setLastName("Roy")
        time.sleep(3)
        self.userManagement.clickRole()
        time.sleep(3)
        self.userManagement.clickActiveStatus()
        time.sleep(3)
        self.userManagement.clickSave_addMember()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text
        print(self.msg)
        if 'Email already exists. Please choose a different email.' in self.msg:
            assert True
            self.logger.info("********* Add Member Test - Invalid - Add Existing Email Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addMember_Invalid_AddExistingEmail_scr.png")  # Screenshot
            self.logger.error("********* Add Member Test - Invalid - Add Existing Email Test Failed ************")
            assert False
        self.driver.close()



