import time

import self
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.RecipesPage import RecipesPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_AddRecipes:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addRecipes(self, setup):
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

        # Add Recipes

        self.rp.clickAddRecipies()
        time.sleep(3)
        self.rp.setName("Smoothies")
        time.sleep(3)
        self.rp.setDescription("Smoothies are thick, creamy beverages usually "
                               "blended from purred fruits, vegetables, "
                               "juices, yogurt, nuts, seeds, and/or dairy or "
                               "nondairy milk.")
        time.sleep(3)
        self.rp.chooseImage()
        time.sleep(3)
        self.rp.clickSave()

        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text
        print(self.msg)
        if 'Audio file required.' in self.msg:
            assert True
            self.logger.info("********* Add Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addRecipies_scr.png")  # Screenshot
            self.logger.error("********* Add Recipes - Test Failed ************")
            assert False

        self.driver.close()
