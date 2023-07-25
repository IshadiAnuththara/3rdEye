import time
from selenium.webdriver.common.by import By
import self as self
from page_objects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLoginNegativeTesting:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    invalid_password = ReadConfig.get_invalid_password()
    logger = LogGen.loggen()
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"

    def test_login_invalid_username_and_password(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login with invalid username and password

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.invalid_username)
        self.lp.set_password(self.invalid_password)
        time.sleep(3)
        self.lp.click_login()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Invalid credentials.' in self.msg:
            assert True
            self.logger.info("********* Login with invalid credentials Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_login_invalid_scr.png")
            self.logger.error("********* Login with invalid credentials Test Failed ************")
            assert False
        self.driver.close()

    def test_login_valid_username_and_invalid_password(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login with valid username and invalid password

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.invalid_password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Invalid credentials.' in self.msg:
            assert True
            self.logger.info("********* Login with invalid credentials Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_login_invalid_scr.png")
            self.logger.error("********* Login with invalid credentials Test Failed ************")
            assert False

        self.driver.close()

    def test_login_invalid_username_valid_password(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login with invalid username and valid password

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.invalid_username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Invalid credentials.' in self.msg:
            assert True
            self.logger.info("********* Login with invalid credentials Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_login_invalid_scr.png")
            self.logger.error("********* Login with invalid credentials Test Failed ************")
            assert False
        self.driver.close()

    def test_login_no_inputs(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login with no inputs

        self.lp = LoginPage(self.driver)
        self.lp.set_username("")
        self.lp.set_password("")
        time.sleep(3)
        self.lp.click_login()

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Missing credentials' in self.msg:
            assert True
            self.logger.info("********* Login with invalid credentials Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_login_invalid_scr.png")
            self.logger.error("********* Login with invalid credentials Test Failed ************")
            assert False
        self.driver.close()

    def test_login_only_username(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login with only username

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        time.sleep(3)
        self.lp.click_login()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Missing credentials' in self.msg:
            assert True
            self.logger.info("********* Login with invalid credentials Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_login_invalid_scr.png")
            self.logger.error("********* Login with invalid credentials Test Failed ************")
            assert False
        self.driver.close()

    def test_login_only_password(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login with only password

        self.lp = LoginPage(self.driver)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Missing credentials' in self.msg:
            assert True
            self.logger.info("********* Login with invalid credentials Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_login_invalid_scr.png")
            self.logger.error("********* Login with invalid credentials Test Failed ************")
            assert False
        self.driver.close()
