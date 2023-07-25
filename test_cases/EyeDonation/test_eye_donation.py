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
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()

        # Access Eye Donation
        time.sleep(4)
        self.ed = EyeDonationPage(self.driver)
        self.ed.clickEyeDonation()

        time.sleep(5)
        self.driver.close()

    def test_search_eye_donation(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()

        # Access Eye Donation

        time.sleep(4)
        self.ed = EyeDonationPage(self.driver)
        self.ed.clickEyeDonation()
        time.sleep(3)

        # Search Eye donations by name

        self.ed.setSearch("kavindu")
        time.sleep(3)
        self.ed.clickSearch()
        time.sleep(3)
        self.ed.clickRefresh()

        time.sleep(5)
        self.driver.close()

    def test_view_eye_donation(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()

        # Access Eye Donation
        time.sleep(4)
        self.ed = EyeDonationPage(self.driver)
        self.ed.clickEyeDonation()
        time.sleep(3)

        # View Eye Donation

        self.ed.clickViewEyeDonation()
        time.sleep(5)
        self.ed.clickClose()

        time.sleep(5)
        self.driver.close()

    def test_delete_eye_donation(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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
