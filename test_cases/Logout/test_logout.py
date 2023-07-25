import time
from selenium.webdriver.common.by import By
import self as self
from page_objects.LoginPage import LoginPage
from page_objects.Logout import Logout
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogout:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"

    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(7)

        # Logout

        self.lt = Logout(self.driver)
        self.lt.clickLogout()
        time.sleep(3)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully logged out.' in self.msg:
            assert True
            self.logger.info("********* Logout Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_logout_scr.png")
            self.logger.error("********* Logout Test Failed ************")
            assert False
        time.sleep(5)
        self.driver.close()
