import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from test_data.user_test_data import UserTestData
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.test_utils import (sleep, SHORT_WAIT, perform_add_member_without_filling_any_field_assertion,
                                  MEDIUM_WAIT,
                                  perform_add_member_only_add_email_assertion,
                                  perform_add_member_only_add_email_first_name_last_name_assertion,
                                  perform_add_member_only_add_first_name_assertion,
                                  perform_add_member_only_add_last_name_assertion,
                                  perform_add_member_add_invalid_email_assertion,
                                  perform_add_member_add_existing_user_assertion,
                                  perform_add_member_add_existing_email_assertion,
                                  perform_add_member_without_select_role_and_active_status_assertion,
                                  perform_add_member_without_select_active_status_assertion,
                                  perform_add_member_only_select_role_assertion,
                                  perform_only_add_password_assertion,
                                  perform_add_member_only_add_username_assertion,
                                  perform_add_member_only_select_active_status_assertion)


class TestUserManagementNegativeTesting:
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
        self.user_management = UserPage(self.driver)
        sleep(SHORT_WAIT)
        self.user_management.click_user()
        sleep(SHORT_WAIT)
        self.user_management.click_user_management()
        sleep(MEDIUM_WAIT)
        yield
        self.driver.close()

    def test_negative_testing_001(self):
        self.user_management.negative_testing_add_member_without_filling_any_field()

        # Define the expected success message
        success_message = 'Email required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_without_filling_any_field_assertion(self.driver, self.user_management, self.logger,
                                                               success_message)

    def test_negative_testing_002(self):
        self.user_management.negative_testing_add_member_only_add_email(UserTestData.email)

        # Define the expected success message
        success_message = 'Username required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_only_add_email_assertion(self.driver, self.user_management, self.logger, success_message)

    def test_negative_testing_003(self):
        self.user_management.negative_testing_add_member_only_add_email_first_name_last_name(
            UserTestData.negative_testing_data_email,
            UserTestData.negative_testing_data_first_name,
            UserTestData.negative_testing_data_last_name)

        # Define the expected success message
        success_message = 'Username required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_only_add_email_first_name_last_name_assertion(self.driver, self.user_management,
                                                                         self.logger, success_message)

    def test_negative_testing_004(self, setup):
        self.user_management.negative_testing_add_member_only_add_first_name(
            UserTestData.negative_testing_data_first_name
        )

        # Define the expected success message
        success_message = 'Email required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_only_add_first_name_assertion(self.driver, self.user_management, self.logger,
                                                         success_message)

    def test_negative_testing_005(self):
        self.user_management.negative_testing_add_member_only_add_last_name(
            UserTestData.negative_testing_data_last_name
        )

        # Define the expected success message
        success_message = 'Email required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_only_add_last_name_assertion(self.driver, self.user_management, self.logger, success_message)

    def test_negative_testing_006(self):
        self.user_management.negative_testing_add_member_only_add_password()

        # Define the expected success message
        success_message = 'Email required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_only_add_password_assertion(self.driver, self.user_management, self.logger, success_message)

    def test_negative_testing_007(self):
        self.user_management.negative_testing_add_member_only_add_username(
            UserTestData.negative_testing_data_username
        )

        # Define the expected success message
        success_message = 'Email required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_only_add_username_assertion(self.driver, self.user_management, self.logger, success_message)

    def test_negative_testing_008(self, setup):
        self.user_management.negative_testing_add_member_only_add_user_name_and_password(
            UserTestData.negative_testing_data_username
        )

        # Define the expected success message
        success_message = 'Email required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_only_add_username_assertion(self.driver, self.user_management, self.logger, success_message)

    def test_negative_testing_009(self):
        self.user_management.negative_testing_add_member_only_select_active_status()

        # Define the expected success message
        success_message = 'Email required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_only_select_active_status_assertion(self.driver, self.user_management, self.logger,
                                                               success_message)

    def test_negative_testing_010(self):
        self.user_management.negative_testing_add_member_only_select_role()

        # Define the expected success message
        success_message = 'Email required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_only_select_role_assertion(self.driver, self.user_management,
                                                      self.logger, success_message)

    def test_add_member_without_select_active_status(self):
        self.user_management.negative_testing_add_member_without_select_active_status(
            UserTestData.negative_testing_data_username,
            UserTestData.negative_testing_data_email,
            UserTestData.negative_testing_data_first_name,
            UserTestData.negative_testing_data_last_name
        )

        # Define the expected success message
        success_message = 'Status required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_without_select_active_status_assertion(self.driver, self.user_management,
                                                                  self.logger, success_message)

    def test_add_member_without_select_role_and_active_status(self):
        self.user_management.negative_testing_add_member_without_select_role_and_active_status(
            UserTestData.negative_testing_data_username,
            UserTestData.negative_testing_data_email,
            UserTestData.negative_testing_data_first_name,
            UserTestData.negative_testing_data_last_name
        )

        # Define the expected success message
        success_message = 'Role required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_without_select_role_and_active_status_assertion(self.driver, self.user_management,
                                                                           self.logger, success_message)

    def test_add_member_add_existing_email(self):
        self.user_management.negative_testing_add_member_add_existing_email(
            UserTestData.negative_testing_data_username,
            UserTestData.negative_testing_data_email,
            UserTestData.negative_testing_data_first_name,
            UserTestData.negative_testing_data_last_name
        )

        # Define the expected success message
        success_message = 'Email already exists. Please choose a different email.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_add_existing_email_assertion(self.driver, self.user_management, self.logger, success_message)

    def test_add_member_add_existing_user(self):
        self.user_management.negative_testing_add_member_add_existing_user(
            UserTestData.negative_testing_data_username,
            UserTestData.negative_testing_data_email,
            UserTestData.negative_testing_data_first_name,
            UserTestData.negative_testing_data_last_name
        )

        # Define the expected success message
        success_message = 'Username already exists. Please choose a different name.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_add_existing_user_assertion(self.driver, self.user_management, self.logger, success_message)

    def test_add_member_add_invalid_email(self):
        self.user_management.negative_testing_add_member_add_invalid_email(
            UserTestData.negative_testing_data_username,
            UserTestData.negative_testing_data_email,
            UserTestData.negative_testing_data_first_name,
            UserTestData.negative_testing_data_last_name
        )

        # Define the expected success message
        success_message = 'Email invalid.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_add_invalid_email_assertion(self.driver, self.user_management, self.logger, success_message)
