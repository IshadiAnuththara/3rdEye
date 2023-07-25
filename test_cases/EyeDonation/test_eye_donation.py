import time
import self as self
from selenium.webdriver.common.by import By

from page_objects.EyeDonationPage import EyeDonationPage
from page_objects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestEyeDonation:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"

    def test_access_eye_donation(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()

        # Access Eye Donation
        time.sleep(4)
        self.ed = EyeDonationPage(self.driver)
        self.ed.click_eye_donation()

        time.sleep(5)
        self.driver.close()

    def test_search_eye_donation(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()

        # Access Eye Donation

        time.sleep(4)
        self.ed = EyeDonationPage(self.driver)
        self.ed.click_eye_donation()
        time.sleep(3)

        # Search Eye donations by name

        self.ed.set_search("kavindu")
        time.sleep(3)
        self.ed.click_search()
        time.sleep(3)
        self.ed.click_refresh()

        time.sleep(5)
        self.driver.close()

    def test_view_eye_donation(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()

        # Access Eye Donation
        time.sleep(4)
        self.ed = EyeDonationPage(self.driver)
        self.ed.click_eye_donation()
        time.sleep(3)

        # View Eye Donation

        self.ed.click_view_eye_donation()
        time.sleep(5)
        self.ed.click_close()

        time.sleep(5)
        self.driver.close()

    def test_delete_eye_donation(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(4)

        # Access Eye Donation

        self.ed = EyeDonationPage(self.driver)
        self.ed.click_eye_donation()
        time.sleep(3)

        # Delete Eye Donation

        self.ed.click_delete()

        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text

        print(self.msg)
        if 'Successfully Deleted.' in self.msg:
            assert True
            self.logger.info("********* Delete Eye Donation Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_deleteEyeDonation_scr.png")
            self.logger.error("********* Delete Eye Donation Test Failed ************")
            assert False

        self.driver.close()
