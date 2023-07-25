import time
import self as self
from selenium.webdriver.common.by import By
from page_objects.LoginPage import LoginPage
from page_objects.BannersPage import BannersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestBanners:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    notification = "//div[@class='notifyjs-corner']"

    def test_access_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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
        self.logger.info("********* Access Banners - Test Passed *********")
        time.sleep(5)
        self.driver.close()

    def test_add_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully created.' in self.msg:
            assert True
            self.logger.info("********* Add Banner Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addBanner_scr.png")  # Screenshot
            self.logger.error("********* Add Banner Test Failed ************")
            assert False
        self.driver.close()

    def test_close_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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
        self.msg = self.driver.find_element(By.XPATH, self.notification).text

        print(self.msg)
        if 'Successfully deleted.' in self.msg:
            assert True
            self.logger.info("********* Close banners Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_closeBanners_scr.png")  # Screenshot
            self.logger.error("********* Close banners Test Failed ************")
            assert False
        self.driver.close()

    def test_edit_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully updated' in self.msg:
            assert True
            self.logger.info("********* Edit Banner Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_editBanner_scr.png")  # Screenshot
            self.logger.error("********* Edit Banner Test Failed ************")
            assert False
        self.driver.close()

    def test_show_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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
        time.sleep(5)

        # Show Banners

        self.banners.clickCheckbox()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully updated' in self.msg:
            assert True
            self.logger.info("********* Show Banner Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_showBanner_scr.png")  # Screenshot
            self.logger.error("********* Show Banner Test Failed ************")
            assert False
        self.driver.close()

    def test_delete_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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

        # Delete Banners

        self.banners.clickDelete()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully deleted.' in self.msg:
            assert True
            self.logger.info("********* Delete Banner Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_deleteBanner_scr.png")  # Screenshot
            self.logger.error("********* Delete Banner Test Failed ************")
            assert False
        self.driver.close()
