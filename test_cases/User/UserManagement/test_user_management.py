import time
from selenium.webdriver.common.by import By
import self as self
from page_objects.LoginPage import LoginPage
from page_objects.UserPage import UserPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestUserManagement:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    name = "TestUser007"
    email = "mar.is.saa.l.d.a0@gmail.com"
    first_name = "Brielle"
    last_name = "Roy"
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"
    search_name = "superAdmin"

    def test_access_user_management(self, setup):
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

        self.um = UserPage(self.driver)
        self.um.clickUser()
        time.sleep(3)

        # Access User Management

        self.um.clickUserManagement()

        time.sleep(4)
        self.driver.close()

    def test_add_member(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.clickUser()
        time.sleep(3)

        # Access User Management

        self.userManagement.clickUserManagement()
        time.sleep(3)

        # Add Member

        self.userManagement.clickAddMember()
        time.sleep(2)
        self.userManagement.setUsername(self.name)
        time.sleep(3)
        self.userManagement.clickGeneratePassword()
        time.sleep(5)
        self.userManagement.setEmail(self.email)
        time.sleep(3)
        self.userManagement.setFirstName(self.first_name)
        time.sleep(3)
        self.userManagement.setLastName(self.last_name)
        time.sleep(3)
        self.userManagement.clickRole()
        time.sleep(3)
        self.userManagement.clickActiveStatus()
        time.sleep(3)
        self.userManagement.clickSave_addMember()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully created.' in self.msg:
            assert True
            self.logger.info("********* Add Member Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addMember_scr.png")
            self.logger.error("********* Add Member Test Failed ************")
            assert False
        self.driver.close()

    def test_search_user(self, setup):
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

        self.userManagement = UserPage(self.driver)
        self.userManagement.clickUser()
        time.sleep(3)

        # Access User Management

        self.userManagement.clickUserManagement()
        time.sleep(3)

        # Search User

        self.userManagement.setSearch(self.search_name)
        time.sleep(2)
        self.userManagement.clickSearch()
        time.sleep(3)
        self.userManagement.clickRefresh()
        time.sleep(4)
        self.driver.close()
