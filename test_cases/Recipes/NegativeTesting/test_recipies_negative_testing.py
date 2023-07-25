import time
import self
from selenium.webdriver.common.by import By
from page_objects.LoginPage import LoginPage
from page_objects.RecipesPage import RecipesPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestRecipesNegativeTesting:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    notification = "//div[@class='notifyjs-corner']"
    screenshot = ".\\Screenshots\\"
    name = "Smoothies"
    description = "Smoothies are thick, creamy beverages usually blended from purred fruits, vegetables, juices, " \
                  "yogurt, nuts, seeds, and/or dairy or nondairy milk."

    def test_add_recipes_without_fill_any_field(self, setup):
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
        self.rp.click_save()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Name required.' in self.msg:
            assert True
            self.logger.info("********* Add Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addRecipies_scr.png")
            self.logger.error("********* Add Recipes - Test Failed ************")
            assert False
        self.driver.close()

    def test_add_recipes_only_fill_name(self, setup):
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
        self.rp.click_save()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Audio file required.' in self.msg:
            assert True
            self.logger.info("********* Add Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addRecipies_scr.png")
            self.logger.error("********* Add Recipes - Test Failed ************")
            assert False
        self.driver.close()

    def test_add_recipes_only_add_audio(self, setup):
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
        self.rp.add_audio()
        time.sleep(3)
        self.rp.click_save()
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Name required.' in self.msg:
            assert True
            self.logger.info("********* Add Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addRecipies_scr.png")
            self.logger.error("********* Add Recipes - Test Failed ************")
            assert False
        self.driver.close()

    def test_add_recipes_add_spaces_for_name(self, setup):
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
        self.rp.set_name("                                                 ")
        time.sleep(3)
        self.rp.set_description(self.description)
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
            self.driver.save_screenshot(self.screenshot + "test_addRecipies_scr.png")
            assert True
            self.logger.error("********* Add Recipes - Test Failed ************")
        else:
            self.logger.info("********* Add Recipes - Test Passed *********")
            assert False

        self.driver.close()

    def test_add_recipes_only_add_name_and_description(self, setup):
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
        self.rp.set_description(self.description)
        time.sleep(3)

        self.rp.click_save()

        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Audio file required.' in self.msg:
            assert True
            self.logger.info("********* Add Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addRecipies_scr.png")
            self.logger.error("********* Add Recipes - Test Failed ************")
            assert False

        self.driver.close()

    def test_add_recipes_without_add_audio(self, setup):
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
        self.rp.set_description(self.description)
        time.sleep(3)
        self.rp.choose_image()
        time.sleep(3)
        self.rp.click_save()

        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, self.notification).text
        print(self.msg)
        if 'Audio file required.' in self.msg:
            assert True
            self.logger.info("********* Add Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(self.screenshot + "test_addRecipies_scr.png")
            self.logger.error("********* Add Recipes - Test Failed ************")
            assert False

        self.driver.close()
