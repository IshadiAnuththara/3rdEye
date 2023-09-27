import pytest
import self as self
from test_data.eye_donation_test_data import EyeDonationTestData
from pageObjects.EyeDonationPage import EyeDonationPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.test_utils import sleep, MEDIUM_WAIT, SHORT_WAIT, perform_add_new_recipe_assertion


class TestEyeDonation:
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

        # Initialize the LoginPage object and perform login
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(MEDIUM_WAIT)

        # Initialize the Eye donation Page object
        self.eye_donation = EyeDonationPage(self.driver)
        sleep(SHORT_WAIT)
        self.eye_donation.click_eye_donation()
        sleep(MEDIUM_WAIT)
        yield
        self.driver.close()

    def test_search_eye_donation(self):
        self.eye_donation.search_eye_donation(EyeDonationTestData.name)

    def test_view_eye_donation(self):
        self.eye_donation.click_view_eye_donation()

    def test_delete_eye_donation(self):
        self.eye_donation.click_delete()
        # Define the expected success message
        success_message = 'Successfully Deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete eye donation
        perform_add_new_recipe_assertion(self.driver, self.eye_donation, self.logger, success_message)
