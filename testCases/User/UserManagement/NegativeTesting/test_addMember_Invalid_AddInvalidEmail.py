import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AddMember_Invalid_AddInvalidEmail:
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
        self.userManagement.setUsername("TestUser007")
        time.sleep(3)
        self.userManagement.clickGeneratePassword()
        time.sleep(5)
        self.userManagement.setEmail("castielv.i.nc.en.t.36.9@gmail@gmail.com")
        time.sleep(3)
        self.userManagement.setFirstName("Jennie")
        time.sleep(3)
        self.userManagement.setLastName("Medina")
        time.sleep(3)
        self.userManagement.clickRole()
        time.sleep(3)
        self.userManagement.clickActiveStatus()
        time.sleep(3)
        self.userManagement.clickSave_addMember()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text
        print(self.msg)
        if 'Email invalid.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid - Add Invalid Email Test Passed *********")
        elif 'Successfully created.':
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addMember_Invalid_AddInvalidEmail_scr.png")  # Screenshot
            self.logger.error("********* Add Member - Invalid - Add Invalid Email Test Failed ************")
            assert False
        self.driver.close()


