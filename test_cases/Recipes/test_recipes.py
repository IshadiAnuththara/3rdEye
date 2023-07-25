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
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(5)

        # Access Recipes

        self.rp = RecipesPage(self.driver)
        self.rp.click_recipies()
        time.sleep(3)
        self.driver.close()

    def test_add_recipes(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(5)

        # Access Recipes

        self.rp = RecipesPage(self.driver)
        self.rp.click_recipies()
        time.sleep(3)

        # Add Recipes

        self.rp.click_add_recipies()
        time.sleep(3)
        self.rp.set_name(self.name)
        time.sleep(3)
        self.rp.set_description(self.desc)
        time.sleep(3)
        self.rp.choose_image()
        time.sleep(3)
        self.rp.add_audio()
        time.sleep(3)
        self.rp.click_save()
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
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(5)

        # Access Recipes

        self.rp = RecipesPage(self.driver)
        self.rp.click_recipies()
        time.sleep(3)

        # Edit Recipes

        self.rp.click_edit()
        time.sleep(3)
        self.rp.edit_image()
        time.sleep(3)
        self.rp.click_save()

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
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(5)

        # Access Recipes

        self.rp = RecipesPage(self.driver)
        self.rp.click_recipies()
        time.sleep(3)

        # Search Recipes

        self.rp.search_recipies(self.search_recipe)
        time.sleep(3)
        self.rp.click_refresh()
        time.sleep(5)
        self.driver.close()

    def test_delete_recipies(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(5)

        # Access Recipes

        self.rp = RecipesPage(self.driver)
        self.rp.click_recipies()
        time.sleep(3)

        # Delete Recipes

        self.rp.click_delete()

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
