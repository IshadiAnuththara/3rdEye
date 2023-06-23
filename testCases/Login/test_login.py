import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Login:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    invalidUsername = ReadConfig.getInvalidUsername()
    invalidPassword = ReadConfig.getInvalidPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()

        time.sleep(3)

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text

        print(self.msg)
        if 'Successfully logged in.' in self.msg:
            assert True
            self.logger.info("********* Login with valid credentials Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_scr.png")  # Screenshot
            self.logger.error("********* Login with valid credentials Test Failed ************")
            assert False

        time.sleep(5)

        self.driver.close()
