from selenium.webdriver.common.by import By


class Logout:
    input_username_xpath = "//input[@placeholder='Username']"
    input_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "(//button[@class='ant-btn login-form-button login-form-margin w-100 ant-btn-primary'])[1]"
    button_logout_xpath = "/html/body/blind-app-root/blind-app-layout/nz-layout/nz-layout/nz-content/div[1]/button"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.input_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
