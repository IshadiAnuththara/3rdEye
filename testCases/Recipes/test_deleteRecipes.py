import time

import self
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.RecipesPage import RecipesPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_DeleteRecipies:
    baseURL = ReadConfig.getApplication(self)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_deleteRecipies(self, setup):
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

        # Delete Recipes

        self.rp.clickDelete()

        time.sleep(5)
        self.msg = self.driver.find_element(By.XPATH, "//div[@class='notifyjs-corner']").text
        print(self.msg)
        if 'Successfully deleted.' in self.msg:
            assert True
            self.logger.info("********* Delete Recipes - Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_deleteRecipies_scr.png")  # Screenshot
            self.logger.error("********* Delete Recipes - Test Failed ************")
            assert False

        self.driver.close()
