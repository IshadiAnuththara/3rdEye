import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    input_username_xpath = "//input[@placeholder='Username']"
    input_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "(//button[@class='ant-btn login-form-button login-form-margin w-100 ant-btn-primary'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.input_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

