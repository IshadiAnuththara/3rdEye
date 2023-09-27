import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from test_cases.base_test import BaseTest
from test_data.recipes_test_data import RecipesTestData
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.RecipesPage import RecipesPage
from utilities.test_utils import sleep, MEDIUM_WAIT, SHORT_WAIT, perform_add_new_recipe_assertion, \
    perform_edit_recipe_assertion, perform_delete_recipe_assertion


class TestRecipes(BaseTest):
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
