import time
from selenium.webdriver.common.by import By
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.BannersPage import BannersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_EditBanners:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_editBanners(self, setup):
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
        # Edit Banner

        self.banners.clickEdit()
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
        if 'Successfully updated' in self.msg:
            assert True
            self.logger.info("********* Edit Banner Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_editBanner_scr.png")  # Screenshot
            self.logger.error("********* Edit Banner Test Failed ************")
            assert False
        self.driver.close()
