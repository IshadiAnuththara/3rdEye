import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.BannersPage import BannersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.test_utils import (sleep, MEDIUM_WAIT, SHORT_WAIT, perform_add_new_banner_assertion,
                                  perform_close_banners_assertion, perform_edit_banners_assertion,
                                  perform_show_banners_assertion, perform_delete_banners_assertion)


class TestBanners:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):

        # Initialize the WebDriver and navigate to the application
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        # Initialize the Login Page object and perform login
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(MEDIUM_WAIT)

        # Initialize the Banners Page object
        self.banners = BannersPage(self.driver)
        sleep(SHORT_WAIT)
        self.banners.click_banners()
        sleep(MEDIUM_WAIT)
        yield
        self.driver.close()

    def test_add_banners(self):
        self.banners.add_new_banner()
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new banner creation
        perform_add_new_banner_assertion(self.driver, self.banners, self.logger, success_message)

    def test_close_banners(self):
        self.banners.close_banners()
        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate close banners
        perform_close_banners_assertion(self.driver, self.banners, self.logger, success_message)

    def test_edit_banners(self):
        self.banners.edit_banners()
        # Define the expected success message
        success_message = 'Successfully updated'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit banners
        perform_edit_banners_assertion(self.driver, self.banners, self.logger, success_message)

    def test_show_banners(self):
        self.banners.click_checkbox()
        sleep(SHORT_WAIT)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate show banners
        perform_show_banners_assertion(self.driver, self.banners, self.logger, success_message)

    def test_delete_banners(self):
        self.banners.click_delete()
        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete banners
        perform_delete_banners_assertion(self.driver, self.banners, self.logger, success_message)
