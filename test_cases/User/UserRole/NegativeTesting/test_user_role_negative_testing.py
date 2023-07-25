import time
from selenium.webdriver.common.by import By
import self as self
from page_objects.LoginPage import LoginPage
from page_objects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AddUserRole_Invalid_WithoutEnterAnyField:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"

    def test_add_user_role_without_enter_any_field(self, setup):
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
        time.sleep(2)
        self.ur.clickSave()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Role name required.' in self.msg:
            assert True
            self.logger.info("********* Add User Role - Without Enter Any Field Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_Invalid_WithoutEnterAnyField_scr.png")  # Screenshot
            self.logger.error("********* Add User Role - Without Enter Any Field Test Failed ************")
            assert False
        self.driver.close()

    def test_add_user_role_only_add_user_role(self, setup):
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
        self.ur.setRole("Test User_002")
        time.sleep(3)
        self.ur.clickSave()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Permissions required.' in self.msg:
            assert True
            self.logger.info("********* Add User Role - Only Add User Role Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addUserRole_Invalid_OnlyAddUserRole_scr.png")  # Screenshot
            self.logger.error("********* Add User Role - Only Add User Role Test Failed ************")
            assert False
        self.driver.close()

    def test_add_user_role_only_add_permissions(self, setup):
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
        if 'Role name required.' in self.msg:
            assert True
            self.logger.info("********* Add User Role - OnlyAddPermissions Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addUserRole_Invalid_OnlyAddPermissions_scr.png")  # Screenshot
            self.logger.error("********* Add User Role - OnlyAddPermissions Test Failed ************")
            assert False
        self.driver.close()

    def test_add_user_role_existing_user_role(self, setup):
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
        if 'Role already exists. Please choose a different name.' in self.msg:
            assert True
            self.logger.info("********* Add User Role - Existing User Role Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addUserRole_Invalid_ExistingUserRole_scr.png")  # Screenshot
            self.logger.error("********* Add User Role - Existing User Role  Test Failed ************")
            assert False
        self.driver.close()


