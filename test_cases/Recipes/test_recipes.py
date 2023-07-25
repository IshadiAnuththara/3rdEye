import time
import self as self
from selenium.webdriver.common.by import By

from page_objects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from page_objects.RecipesPage import RecipesPage


class TestRecipes:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    name = "Smoothies"
    desc = "Smoothies are thick, creamy beverages usually blended from purred fruits, vegetables, juices, yogurt, " \
           "nuts, seeds, and/or dairy or nondairy milk."
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"
    search_recipe = "Fried Chicken Leg and Chicken Tempura with Spicy Mayonnaise and Fries"

    def test_access_recipes(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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
        self.driver.close()

    def test_add_recipes(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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

        # Add Recipes

        self.rp.clickAddRecipies()
        time.sleep(3)
        self.rp.setName(self.name)
        time.sleep(3)
        self.rp.setDescription(self.desc)
        time.sleep(3)
        self.rp.chooseImage()
        time.sleep(3)
        self.rp.addAudio()
        time.sleep(3)
        self.rp.clickSave()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully created.' in self.msg:
            assert True
            self.logger.info("********* Add Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addRecipies_scr.png")
            self.logger.error("********* Add Recipes - Test Failed ************")
            assert False

        self.driver.close()

    def test_edit_recipies(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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

        # Edit Recipes

        self.rp.clickEdit()
        time.sleep(3)
        self.rp.editImage()
        time.sleep(3)
        self.rp.clickSave()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully updated.' in self.msg:
            assert True
            self.logger.info("********* Edit Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_editRecipies_scr.png")
            self.logger.error("********* Edit Recipes - Test Failed ************")
            assert False

        self.driver.close()

    def test_search_recipies(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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

        self.rp.searchRecipies(self.search_recipe)
        time.sleep(3)
        self.rp.clickRefresh()
        time.sleep(5)
        self.driver.close()

    def test_delete_recipies(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

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

        # Delete Recipes

        self.rp.clickDelete()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Successfully deleted.' in self.msg:
            assert True
            self.logger.info("********* Delete Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_deleteRecipies_scr.png")
            self.logger.error("********* Delete Recipes - Test Failed ************")
            assert False

        self.driver.close()
