import time
from selenium.webdriver.common.by import By
import self as self
from page_objects.LoginPage import LoginPage
from page_objects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestUserManagementNegativeTesting:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"

    def test_add_member_without_filling_any_field(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Without filling any field

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Without Fill Any Field Test Passed *********")
        else:
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_WithoutFillAnyField_scr.png")  # Screenshot
            self.logger.error("********* Add Member - Without Fill Any Field Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_only_add_email(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_email("lamax73497@extemer.com")
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Username required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Only Add Email Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addMember_Invalid_OnlyAddEmail_scr.png")
            self.logger.error("********* Add Member - Only Add Email Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_only_add_email_first_name_last_name(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_email("miwabog446@fitwl.com")
        time.sleep(3)
        self.userManagement.set_first_name("Brielle")
        time.sleep(3)
        self.userManagement.set_last_name("Roy")
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Username required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid_Only Add Email,FirstName, and LastName Test Passed "
                             "*********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addMember_"
                                                          "Invalid_OnlyAddEmail_FirstName_LastName_scr.png")
            self.logger.error("*********  Add Member - Invalid_Only Add Email,FirstName, and LastName Test Failed "
                              "************")
            assert False
        self.driver.close()

    def test_add_member_only_add_first_name(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_first_name("Sarah")
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid - Only Add First Name Test Passed *********")
        else:
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_OnlyAddFirstName_scr.png")
            self.logger.error("********* Add Member - Invalid - Only Add First Name Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_only_add_last_name(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_last_name("Price")
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid - Only Add Last Name Test Passed *********")
        else:
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_OnlyAddLastName_scr.png")
            self.logger.error("********* Add Member - Invalid - Only Add Last Name Test Failed ************")
            assert False
        self.driver.close()

    def test_addMember(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.click_generate_password()
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid Only Add Password Test Passed *********")
        else:
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_OnlyAddPassword_scr.png")
            self.logger.error("********* Add Member - Invalid Only Add Password Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_only_add_username(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_username("testUser")
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid Only Add Username Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test__Invalid_OnlyAddUsername_scr.png")
            self.logger.error("********* Add Member - Invalid Only Add Username Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_only_add_user_name_and_password(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_username("testUser")
        time.sleep(3)
        self.userManagement.click_generate_password()
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid - Only Add Username And Password Test Passed *********")
        else:
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_OnlyAddUsernameAndPassword_scr.png")
            self.logger.error(
                "********* Add Member - Invalid - Only Add Username And Password Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_only_select_active_status(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.click_active_status()
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid - Only Select Active Status Test Passed *********")
        else:
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_OnlySelectActiveStatus_scr.png")
            self.logger.error("********* Add Member - Invalid - Only Select Active Status Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_only_select_role(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.click_role()
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid - Only Select Role Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addMember_Invalid_OnlySelectRole_scr.png")
            self.logger.error("********* Add Member - Invalid - Only Select Role Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_without_select_active_status(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_username("testUser")
        time.sleep(3)
        self.userManagement.click_generate_password()
        time.sleep(5)
        self.userManagement.set_email("miwabog446@fitwl.com")
        time.sleep(3)
        self.userManagement.set_first_name("Brielle")
        time.sleep(3)
        self.userManagement.set_last_name("Roy")
        time.sleep(3)
        self.userManagement.click_role()
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Status required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid - Without Select Active Status Test Passed *********")
        else:
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_WithoutSelectActiveStatus_scr.png")
            self.logger.error("********* Add Member - Invalid - Without Select Active Status Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_without_select_role_and_active_status(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_username("testUser")
        time.sleep(3)
        self.userManagement.click_generate_password()
        time.sleep(5)
        self.userManagement.set_email("miwabog446@fitwl.com")
        time.sleep(3)
        self.userManagement.set_first_name("Brielle")
        time.sleep(3)
        self.userManagement.set_last_name("Roy")
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Role required.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid Without SelectRole And ActiveStatus Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addMember_Invalid_WithoutSelectRole"
                                                          "_And_ActiveStatus_scr.png")
            self.logger.error("********* Add Member - Invalid Without SelectRole "
                              "And ActiveStatus Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_add_existing_email(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_username("TestUser")
        time.sleep(3)
        self.userManagement.click_generate_password()
        time.sleep(5)
        self.userManagement.set_email("miwabog446@fitwl.com")
        time.sleep(3)
        self.userManagement.set_first_name("Brielle")
        time.sleep(3)
        self.userManagement.set_last_name("Roy")
        time.sleep(3)
        self.userManagement.click_role()
        time.sleep(3)
        self.userManagement.click_active_status()
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email already exists. Please choose a different email.' in self.msg:
            assert True
            self.logger.info("********* Add Member Test - Invalid - Add Existing Email Test Passed *********")
        else:
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_AddExistingEmail_scr.png")
            self.logger.error("********* Add Member Test - Invalid - Add Existing Email Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_add_existing_user(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_username("TestUser")
        time.sleep(3)
        self.userManagement.click_generate_password()
        time.sleep(5)
        self.userManagement.set_email("sam.ue.le.r.utte.r.4.14@gmail.com")
        time.sleep(3)
        self.userManagement.set_first_name("Brielle")
        time.sleep(3)
        self.userManagement.set_last_name("Roy")
        time.sleep(3)
        self.userManagement.click_role()
        time.sleep(3)
        self.userManagement.click_active_status()
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Username already exists. Please choose a different name.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid - Add Existing User Test Passed *********")
        else:
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_AddExistingUser_scr.png")
            self.logger.error("********* Add Member - Invalid - Add Existing User Test Failed ************")
            assert False
        self.driver.close()

    def test_add_member_add_invalid_email(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.click_user()
        time.sleep(3)

        # Access User Management

        self.userManagement.click_user_management()
        time.sleep(3)

        # Add Member

        self.userManagement.click_add_member()
        time.sleep(2)
        self.userManagement.set_username("TestUser007")
        time.sleep(3)
        self.userManagement.click_generate_password()
        time.sleep(5)
        self.userManagement.set_email("castielv.i.nc.en.t.36.9@gmail@gmail.com")
        time.sleep(3)
        self.userManagement.set_first_name("Jennie")
        time.sleep(3)
        self.userManagement.set_last_name("Medina")
        time.sleep(3)
        self.userManagement.click_role()
        time.sleep(3)
        self.userManagement.click_active_status()
        time.sleep(3)
        self.userManagement.click_save_add_member()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Email invalid.' in self.msg:
            assert True
            self.logger.info("********* Add Member - Invalid - Add Invalid Email Test Passed *********")
        elif 'Successfully created.':
            self.driver.save_screenshot(
                self.screenshot + "test_addMember_Invalid_AddInvalidEmail_scr.png")
            self.logger.error("********* Add Member - Invalid - Add Invalid Email Test Failed ************")
            assert False
        self.driver.close()
