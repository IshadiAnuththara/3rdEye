import time
from selenium.webdriver.common.by import By
import self as self
from page_objects.LoginPage import LoginPage
from page_objects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestUserRoleNegativeTesting:
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
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(2)

        # Access User

        self.ur = UserPage(self.driver)
        self.ur.click_user()
        time.sleep(3)

        # Access User Role

        self.ur.click_user_role()

        # Add new User Role
        self.ur.click_add_user_role()
        time.sleep(2)
        self.ur.click_save()

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
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(2)

        # Access User

        self.ur = UserPage(self.driver)
        self.ur.click_user()
        time.sleep(3)

        # Access User Role

        self.ur.click_user_role()

        # Add new User Role
        self.ur.click_add_user_role()
        time.sleep(3)
        self.ur.set_role("Test User_002")
        time.sleep(3)
        self.ur.click_save()

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
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(2)

        # Access User

        self.ur = UserPage(self.driver)
        self.ur.click_user()
        time.sleep(3)

        # Access User Role

        self.ur.click_user_role()

        # Add new User Role
        self.ur.click_add_user_role()
        time.sleep(3)
        self.ur.click_permission()
        time.sleep(2)
        self.ur.click_permission_user_management()
        time.sleep(2)
        self.ur.click_permission_recipies()
        time.sleep(2)
        self.ur.click_permission_eye_donations()
        time.sleep(2)
        self.ur.click_permission_banners()
        time.sleep(2)
        self.ur.click_save()

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
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(2)

        # Access User

        self.ur = UserPage(self.driver)
        self.ur.click_user()
        time.sleep(3)

        # Access User Role

        self.ur.click_user_role()

        # Add new User Role
        self.ur.click_add_user_role()
        time.sleep(3)
        self.ur.set_role("Test User")
        time.sleep(3)
        self.ur.click_permission()
        time.sleep(2)
        self.ur.click_permission_user_management()
        time.sleep(2)
        self.ur.click_permission_recipies()
        time.sleep(2)
        self.ur.click_permission_eye_donations()
        time.sleep(2)
        self.ur.click_permission_banners()
        time.sleep(2)
        self.ur.click_save()

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


