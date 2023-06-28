import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.BannersPage import BannersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AddBanners:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addBanners(self, setup):
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

        # Add Banner

        self.banners.clickAddBanner()
        time.sleep(3)
        self.banners.clickUpload()
        time.sleep(3)
        self.banners.clickChooseImage()
        time.sleep(3)
        self.banners.clickAdd()
        time.sleep(3)
        self.banners.clickSave()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text
        print(self.msg)
        if 'Successfully created.' in self.msg:
            assert True
            self.logger.info("********* Add Banner Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addBanner_scr.png")  # Screenshot
            self.logger.error("********* Add Banner Test Failed ************")
            assert False
        self.driver.close()

