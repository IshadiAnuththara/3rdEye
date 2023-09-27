import time
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.Logout import Logout
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.test_utils import perform_logout_assertion


class TestLogout:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.login = LoginPage(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.password)
        time.sleep(3)
        self.login.click_login()
        time.sleep(7)

        # Logout

        self.logout = Logout(self.driver)
        self.logout.click_logout()
        time.sleep(3)

        # Define the expected success message
        success_message = 'Successfully logged out.'
        # Call the assertion function to validate login
        perform_logout_assertion(self.driver, self.logout, self.logger, success_message)
        self.driver.close()
