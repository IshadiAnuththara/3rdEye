import time
from selenium.webdriver.common.by import By
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.Logout import Logout
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Logout:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

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

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text

        print(self.msg)
        if 'Successfully logged out.' in self.msg:
            assert True
            self.logger.info("********* Logout Test Passed *********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout_scr.png")  # Screenshot
            self.logger.error("********* Logout Test Failed ************")

            assert False

        time.sleep(5)
        self.driver.close()
