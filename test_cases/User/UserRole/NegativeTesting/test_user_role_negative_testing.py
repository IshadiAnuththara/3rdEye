import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from test_data.user_test_data import UserTestData
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.test_utils import sleep, MEDIUM_WAIT, SHORT_WAIT, \
    perform_add_user_role_without_enter_any_field_assertion, perform_add_user_role_only_add_user_role_assertion, \
    perform_add_user_role_only_add_permissions_assertion, perform_logout_assertion


class TestUserRoleNegativeTesting:
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

    def test_negative_testing_001(self):
        self.user_role.negative_testing_add_user_role_without_enter_any_field()

        # Define the expected success message
        success_message = 'Role name required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_user_role_without_enter_any_field_assertion(self.driver, self.user_role,
                                                                self.logger, success_message)

    def test_negative_testing_002(self):
        self.user_role.negative_testing_add_user_role_only_add_user_role(UserTestData.role)

        # Define the expected success message
        success_message = 'Permissions required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_user_role_only_add_user_role_assertion(self.driver, self.user_role,
                                                           self.logger, success_message)

    def test_negative_testing_003(self, setup):
        self.user_role.negative_testing_add_user_role_only_add_permissions()
        # Define the expected success message
        success_message = 'Role name required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_user_role_only_add_permissions_assertion(self.driver, self.user_role,
                                                             self.logger, success_message)

    def test_negative_testing_004(self):
        self.user_role.negative_testing_add_user_role_existing_user_role(
            UserTestData.role
        )
        # Define the expected success message
        success_message = 'Role already exists. Please choose a different name.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_logout_assertion(self.driver, self.user_role, self.logger, success_message)
