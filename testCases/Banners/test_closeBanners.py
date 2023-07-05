import time
from selenium.webdriver.common.by import By
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.BannersPage import BannersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_CloseBanners:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_closeBanners(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(4)

        # Access Banners

        self.banners = BannersPage(self.driver)
        self.banners.clickBanners()
        time.sleep(3)

        # Close banners

        self.banners.clickEdit()
        time.sleep(3)
        self.banners.clickClose()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text

        print(self.msg)
        if 'Successfully deleted.' in self.msg:
            assert True
            self.logger.info("********* Close banners Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_closeBanners_scr.png")  # Screenshot
            self.logger.error("********* Close banners Test Failed ************")
            assert False
        self.driver.close()
