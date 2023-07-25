import time
import pyautogui
from selenium.webdriver.common.by import By


class RecipesPage:
    hyperlink_recipies_xpath = "//a[normalize-space()='Recipes']"
    button_add_recipies_xpath = "//button[@class='ant-btn d-flex align-items-center " \
                                "ant-btn-primary ng-star-inserted']"
    input_name_xpath = "//input[@id='name']"
    textarea_description_xpath = "//textarea[@id='desc']"
    span_choose_image_xpath = "//span[normalize-space()='Choose new image']"
    input_audio_xpath = "//input[@id='audio']"
    span_save_xpath = "//span[normalize-space()='Save']"
    button_delete_xpath = "//tbody/tr[1]/td[3]/nz-space[1]/div[2]/button[1]"
    span_ok_xpath = "//span[normalize-space()='OK']"
    button_edit_xpath = "(//button[@class='ant-btn btn ant-btn-icon-only ng-star-inserted'])[9]"
    input_search_xpath = "//input[@placeholder='Search recipe']"
    button_search_xpath = "(//button[@type='submit'])[1]"
    button_refresh_xpath = "(//button[@class='ant-btn d-flex align-items-center p-0 justify-content-center " \
                           "ng-star-inserted'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_recipies(self):
        self.driver.find_element(By.XPATH, self.hyperlink_recipies_xpath).click()

    def click_add_recipies(self):
        self.driver.find_element(By.XPATH, self.button_add_recipies_xpath).click()

    def set_name(self, name):
        self.driver.find_element(By.XPATH, self.input_name_xpath).send_keys(name)

    def set_description(self, desc):
        self.driver.find_element(By.XPATH, self.textarea_description_xpath).send_keys(desc)

    def choose_image(self):
        self.driver.find_element(By.XPATH, self.span_choose_image_xpath).click()
        time.sleep(3)
        # Set the file path of the AutoIT script
        autoit_script = "C:\\Users\\Ishadi\\Pictures\\3rd eye\\Smoothie.png"
        time.sleep(1)
        pyautogui.typewrite(autoit_script)
        pyautogui.press("enter")

    def add_audio(self):
        self.driver.find_element(By.XPATH, self.input_audio_xpath).send_keys("C:\\Users\\Ishadi\\Pictures\\3rd "
                                                                             "eye\\Recipe Audio\\Recipe-No-006.mp3")

    def click_save(self):
        self.driver.find_element(By.XPATH, self.span_save_xpath).click()

    def click_delete(self):
        self.driver.find_element(By.XPATH, self.button_delete_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.span_ok_xpath).click()

    def click_edit(self):
        # self.edit = self.driver.find_element(By.XPATH, self.button_edit_xpath)
        # self.driver.execute_script("arguments[0].click();", self.edit)

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button_edit_xpath).click()

    def edit_image(self):
        self.driver.find_element(By.XPATH, self.span_choose_image_xpath).click()
        time.sleep(3)
        # Set the file path of the AutoIT script
        autoit_script = "C:\\Users\\Ishadi\\Pictures\\3rd eye\\Test_Smoothies.png"
        time.sleep(1)
        pyautogui.typewrite(autoit_script)
        pyautogui.press("enter")

    def search_recipies(self, name):
        self.driver.find_element(By.XPATH, self.input_search_xpath).send_keys(name)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()

    def click_refresh(self):
        self.driver.find_element(By.XPATH, self.button_refresh_xpath).click()
