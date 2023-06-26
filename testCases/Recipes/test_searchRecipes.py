import time

import self
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.RecipesPage import RecipesPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchRecipes:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchRecipies(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(5)

        # Access Recipes

        self.rp = RecipesPage(self.driver)
        self.rp.clickRecipies()
        time.sleep(3)

        # Search Recipes

        self.rp.searchRecipies("Fried Chicken Leg and Chicken Tempura "
                               "with Spicy Mayonnaise and Fries")
        time.sleep(3)
        self.rp.clickRefresh()
        time.sleep(5)
        self.driver.close()
