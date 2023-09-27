import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from test_data.user_test_data import UserTestData
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_add_new_user_role_assertion, \
    perform_edit_user_role_assertion


class Test_AccessUserRole:
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

        # Initialize the Announcement Page object
        self.user_role = UserPage(self.driver)
        sleep(SHORT_WAIT)
        self.user_role.click_user()
        sleep(SHORT_WAIT)
        self.user_role.click_user_role()
        sleep(MEDIUM_WAIT)
        yield
        self.driver.close()

    def test_add_user_role(self):
        self.user_role.add_new_user_role(UserTestData.role)

        # Define the expected success message
        success_message = 'Successfully Created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_new_user_role_assertion(self.driver, self.user_role, self.logger, success_message)

    def test_edit_user_role(self):
        self.user_role.edit_user_role(UserTestData.edit_role_name)

        # Define the expected success message
        success_message = 'Successfully Created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_edit_user_role_assertion(self.driver, self.user_role, self.logger, success_message)
