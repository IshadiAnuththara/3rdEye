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
    screenshot = ".\\Screenshots\\"

    def test_access_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(4)

        # Access Banners

        self.banners = BannersPage(self.driver)
        self.banners.click_banners()
        time.sleep(5)
        self.driver.close()

    def test_add_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(4)

        # Access Banners

        self.banners = BannersPage(self.driver)
        self.banners.click_banners()

        # Add Banner

        self.banners.click_add_banner()
        time.sleep(3)
        self.banners.click_upload()
        time.sleep(3)
        self.banners.click_choose_image()
        time.sleep(3)
        self.banners.click_add()
        time.sleep(3)
        self.banners.click_save()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully created.' in self.msg:
            assert True
            self.logger.info("********* Add Banner Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addBanner_scr.png")
            self.logger.error("********* Add Banner Test Failed ************")
            assert False
        self.driver.close()

    def test_close_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(4)

        # Access Banners

        self.banners = BannersPage(self.driver)
        self.banners.click_banners()
        time.sleep(3)

        # Close banners

        self.banners.click_edit()
        time.sleep(3)
        self.banners.click_close()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, self.notification).text

        print(self.msg)
        if 'Successfully deleted.' in self.msg:
            assert True
            self.logger.info("********* Close banners Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_closeBanners_scr.png")  # Screenshot
            self.logger.error("********* Close banners Test Failed ************")
            assert False
        self.driver.close()

    def test_edit_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(4)

        # Access Banners

        self.banners = BannersPage(self.driver)
        self.banners.click_banners()
        time.sleep(3)
        # Edit Banner

        self.banners.click_edit()
        time.sleep(3)
        self.banners.click_upload()
        time.sleep(3)
        self.banners.click_choose_image()
        time.sleep(3)
        self.banners.click_add()
        time.sleep(3)
        self.banners.click_save()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully updated' in self.msg:
            assert True
            self.logger.info("********* Edit Banner Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_editBanner_scr.png")
            self.logger.error("********* Edit Banner Test Failed ************")
            assert False
        self.driver.close()

    def test_show_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(4)

        # Access Banners

        self.banners = BannersPage(self.driver)
        self.banners.click_banners()
        time.sleep(5)

        # Show Banners

        self.banners.click_checkbox()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully updated' in self.msg:
            assert True
            self.logger.info("********* Show Banner Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_showBanner_scr.png")
            self.logger.error("********* Show Banner Test Failed ************")
            assert False
        self.driver.close()

    def test_delete_banners(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(4)

        # Access Banners

        self.banners = BannersPage(self.driver)
        self.banners.click_banners()
        time.sleep(3)

        # Delete Banners

        self.banners.click_delete()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully deleted.' in self.msg:
            assert True
            self.logger.info("********* Delete Banner Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_deleteBanner_scr.png")  
            self.logger.error("********* Delete Banner Test Failed ************")
            assert False
        self.driver.close()
