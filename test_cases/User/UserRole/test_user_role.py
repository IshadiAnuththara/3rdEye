import time
from selenium.webdriver.common.by import By
import self as self
from page_objects.LoginPage import LoginPage
from page_objects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AccessUserRole:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"

    def test_access_user_role(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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

        time.sleep(4)
        self.driver.close()

    def test_add_user_role(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully Created.' in self.msg:
            assert True
            self.logger.info("********* Add User Role Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addUserRole_scr.png")  # Screenshot
            self.logger.error("********* Add User Role Test Failed ************")
            assert False
        self.driver.close()

    def test_edit_user_role(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully Updated.' in self.msg:
            assert True
            self.logger.info("********* Edit User Role Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_editUserRole_scr.png")  # Screenshot
            self.logger.error("********* Edit User Role Test Failed ************")
            assert False
        self.driver.close()
