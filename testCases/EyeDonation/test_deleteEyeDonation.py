import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver

from pageObjects.EyeDonationPage import EyeDonationPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_DeleteEyeDonation:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_deleteEyeDonation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(4)

        # Access Eye Donation

        self.ed = EyeDonationPage(self.driver)
        self.ed.clickEyeDonation()
        time.sleep(3)

        # Delete Eye Donation

        self.ed.clickDelete()

        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text

        print(self.msg)
        if 'Successfully Deleted.' in self.msg:
            assert True
            self.logger.info("********* Delete Eye Donation Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_deleteEyeDonation_scr.png")  # Screenshot
            self.logger.error("********* Delete Eye Donation Test Failed ************")
            assert False

        self.driver.close()

