import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from test_data.recipes_test_data import RecipesTestData
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.RecipesPage import RecipesPage
from utilities.test_utils import sleep, MEDIUM_WAIT, SHORT_WAIT, perform_add_new_recipe_assertion, \
    perform_edit_recipe_assertion, perform_delete_recipe_assertion


class TestRecipes:
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

    def test_add_recipes(self):
        self.recipes.add_new_recipe(RecipesTestData.name, RecipesTestData.desc)

        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_add_new_recipe_assertion(self.driver, self.recipes, self.logger, success_message)

    def test_edit_recipies(self):
        self.recipes.edit_recipe()

        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_edit_recipe_assertion(self.driver, self.recipes, self.logger, success_message)

    def test_search_recipies(self):
        self.recipes.search_recipes(RecipesTestData.search_recipe)

    def test_delete_recipies(self):
        self.recipes.click_delete()

        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_delete_recipe_assertion(self.driver, self.recipes, self.logger, success_message)
