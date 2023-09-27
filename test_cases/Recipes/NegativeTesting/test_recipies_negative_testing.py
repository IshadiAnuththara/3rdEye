import pytest
import self
from pageObjects.LoginPage import LoginPage
from pageObjects.RecipesPage import RecipesPage
from test_data.recipes_test_data import RecipesTestData
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_add_recipes_without_fill_any_field_assertion, \
    perform_add_recipes_only_fill_name_assertion, perform_add_recipes_only_add_audio_assertion, \
    perform_add_recipes_add_spaces_for_name_assertion, perform_add_recipes_only_add_name_and_description_assertion, \
    perform_add_member_assertion


class TestRecipesNegativeTesting:
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

        # Initialize the Recipes Page object
        self.recipes = RecipesPage(self.driver)
        sleep(SHORT_WAIT)
        self.recipes.click_recipies()
        sleep(MEDIUM_WAIT)
        yield
        self.driver.close()

    def test_negative_testing_001(self):
        self.recipes.negative_testing_add_recipes_without_fill_any_field()

        # Define the expected success message
        success_message = 'Name required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_recipes_without_fill_any_field_assertion(self.driver, self.recipes, self.logger, success_message)

    def test_negative_testing_002(self):
        self.recipes.negative_testing_add_recipes_only_fill_name(RecipesTestData.name)

        # Define the expected success message
        success_message = 'Audio file required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_recipes_only_fill_name_assertion(self.driver, self.recipes, self.logger, success_message)

    def test_negative_testing_003(self):
        self.recipes.negative_testing_add_recipes_only_add_audio(RecipesTestData.upload_audio)

        # Define the expected success message
        success_message = 'Name required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_recipes_only_add_audio_assertion(self.driver, self.recipes, self.logger, success_message)

    def test_negative_testing_004(self):
        self.recipes.negative_testing_add_recipes_add_spaces_for_name(RecipesTestData.name_negative_testing,
                                                                      RecipesTestData.desc,
                                                                      RecipesTestData.upload_audio)

        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_recipes_add_spaces_for_name_assertion(self.driver, self.recipes, self.logger, success_message)

    def test_negative_testing_005(self):
        self.recipes.negative_testing_add_recipes_only_add_name_and_description(RecipesTestData.name,
                                                                                RecipesTestData.desc)
        # Define the expected success message
        success_message = 'Audio file required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_recipes_only_add_name_and_description_assertion(self.driver, self.recipes, self.logger,
                                                                    success_message)

    def test_negative_testing_006(self):
        self.recipes.negative_testing_add_recipes_without_add_audio(RecipesTestData.name,
                                                                    RecipesTestData.desc)

        # Define the expected success message
        success_message = 'Audio file required.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_member_assertion(self.driver, self.recipes, self.logger, success_message)
