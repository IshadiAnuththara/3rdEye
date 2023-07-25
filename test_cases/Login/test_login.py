import time
from selenium.webdriver.common.by import By
import self as self
from page_objects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogin:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text

        print(self.msg)
        if 'Successfully logged in.' in self.msg:
            assert True
            self.logger.info("********* Login with valid credentials Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_login_scr.png")
            self.logger.error("********* Login with valid credentials Test Failed ************")
            assert False

        self.driver.close()
