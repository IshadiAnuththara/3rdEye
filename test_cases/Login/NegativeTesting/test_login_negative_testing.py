import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.test_utils import (sleep, SHORT_WAIT,
                                  perform_login_invalid_credentials_001_assertion,
                                  perform_login_invalid_credentials_002_assertion,
                                  perform_login_invalid_credentials_003_assertion,
                                  perform_login_invalid_credentials_004_assertion)


class TestLoginNegativeTesting:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    invalid_password = ReadConfig.get_invalid_password()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        # Initialize the WebDriver and navigate to the application
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        # Initialize the Login Page object and perform login
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.close()

    # valid username and valid password
    def test_login_invalid_credentials_001(self):
        self.login_page.login_with_valid_username_and_invalid_password(self.username, self.invalid_password)
        # Define the expected success message
        success_message = 'Invalid credentials.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate login
        perform_login_invalid_credentials_001_assertion(self.driver, self.login_page, self.logger, success_message)

    # invalid username and valid password
    def test_login_invalid_credentials_002(self):
        self.login_page.login_with_invalid_username_and_valid_password(self.invalid_username, self.password)
        # Define the expected success message
        success_message = 'Invalid credentials.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate login
        perform_login_invalid_credentials_002_assertion(self.driver, self.login_page, self.logger, success_message)

    # Invalid username and invalid password
    def test_login_invalid_credentials_003(self):
        self.login_page.login_with_invalid_username_and_invalid_password(self.invalid_username, self.invalid_password)
        # Define the expected success message
        success_message = 'Invalid credentials.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate login
        perform_login_invalid_credentials_003_assertion(self.driver, self.login_page, self.logger, success_message)

    # Without enter username and password
    def test_login_invalid_credentials_004(self):
        self.login_page.login_without_enter_username_password()
        # Define the expected success message
        success_message = 'Missing credentials'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate login
        perform_login_invalid_credentials_004_assertion(self.driver, self.login_page, self.logger, success_message)
