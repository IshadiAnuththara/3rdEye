import time
from selenium.webdriver.common.by import By


class UserPage:
    span_user_xpath = "//span[normalize-space()='User']"
    hyperlink_user_management_xpath = "//a[normalize-space()='User Management']"
    hyperlink_user_role_xpath = "//a[normalize-space()='User Role']"
    button_add_user_role_xpath = "//button[@class='ant-btn d-flex align-items-center " \
                                 "ant-btn-primary ng-star-inserted']"
    input_role_xpath = "//input[@id='role-name']"
    permission_xpath = "//*[@id='userForm']/div[2]/nz-form-item/nz-form-control"
    div_user_management_xpath = "//div[normalize-space()='User Management']"
    div_recipies_xpath = "//div[normalize-space()='Recipes']"
    div_eye_donations_xpath = "//div[normalize-space()='EyeDonations']"
    div_banners_xpath = "//div[normalize-space()='Banners']"
    div_body_xpath = "(//div[@class='ant-drawer-body'])[1]"
    button_save_xpath = "//button[@type='submit']"
    button_edit_xpath = "/html/body/blind-app-root/blind-app-layout/nz-layout/nz-layout/nz-content/div[" \
                        "2]/blind-app-roles/div/div/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table" \
                        "/tbody/tr[2]/td[2]/button"
    span_remove_user_management_xpath = "(//span[@class='ant-select-selection-item-remove ng-star-inserted'])[1]"
    span_remove_recipies_xpath = "(//span[@class='ant-select-selection-item-remove ng-star-inserted'])[2]"
    span_add_member_xpath = "//span[contains(text(),'Add member')]"
    input_username_xpath = "//input[@id='username']"
    span_generate_password_xpath = "//span[normalize-space()='Generate Password']"
    input_email_xpath = "//input[@id='email']"
    input_first_name_xpath = "//input[@id='f-name']"
    input_last_name_xpath = "//input[@id='l-name']"
    input_select_role_xpath = "//*[@id='userForm']/div[6]/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top" \
                              "-control/nz-select-search/input"
    div_role_xpath = "//div[normalize-space()='Testing']"
    input_active_status_xpath = "//*[@id='userForm']/div[7]/nz-form-item/nz-form-control/div/div/nz-select/nz-select" \
                                "-top-control/nz-select-search/input"
    div_inactive_xpath = "//div[normalize-space()='Inactive']"
    span_save_xpath = "//span[normalize-space()='Save']"
    input_search_xpath = "//input[@placeholder='Search name']"
    span_search_xpath = "//span[@class='anticon anticon-search']"
    button_refresh_xpath = "(//button[@class='ant-btn d-flex align-items-center p-0 justify-content-center " \
                           "ng-star-inserted'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_user(self):
        self.driver.find_element(By.XPATH, self.span_user_xpath).click()

    def click_user_management(self):
        self.driver.find_element(By.XPATH, self.hyperlink_user_management_xpath).click()

    def click_user_role(self):
        self.driver.find_element(By.XPATH, self.hyperlink_user_role_xpath).click()

    def click_add_user_role(self):
        self.driver.find_element(By.XPATH, self.button_add_user_role_xpath).click()

    def set_role(self, role):
        self.driver.find_element(By.XPATH, self.input_role_xpath).send_keys(role)

    def click_permission(self):
        self.driver.find_element(By.XPATH, self.permission_xpath).click()

    def click_permission_user_management(self):
        self.driver.find_element(By.XPATH, self.div_user_management_xpath).click()

    def click_permission_recipies(self):
        self.driver.find_element(By.XPATH, self.div_recipies_xpath).click()

    def click_permission_eye_donations(self):
        self.driver.find_element(By.XPATH, self.div_eye_donations_xpath).click()

    def click_permission_banners(self):
        self.driver.find_element(By.XPATH, self.div_banners_xpath).click()

    def click_save(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def click_edit(self):
        self.driver.find_element(By.XPATH, self.button_edit_xpath).click()

    def remove_permission_user_management(self):
        self.driver.find_element(By.XPATH, self.span_remove_user_management_xpath).click()

    def remove_permission_recipies(self):
        self.driver.find_element(By.XPATH, self.span_remove_recipies_xpath).click()

    def edit_role_name(self, name):
        self.driver.find_element(By.XPATH, self.input_role_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.input_role_xpath).send_keys(name)

    def click_add_member(self):
        self.driver.find_element(By.XPATH, self.span_add_member_xpath).click()

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.input_username_xpath).send_keys(username)

    def click_generate_password(self):
        self.driver.find_element(By.XPATH, self.span_generate_password_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(email)

    def set_first_name(self, firstname):
        self.driver.find_element(By.XPATH, self.input_first_name_xpath).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(By.XPATH, self.input_last_name_xpath).send_keys(lastname)

    def click_role(self):
        self.driver.find_element(By.XPATH, self.input_select_role_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.div_role_xpath).click()

    def click_active_status(self):
        self.active_status = self.driver.find_element(By.XPATH, self.input_active_status_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.active_status)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.div_inactive_xpath).click()

    def click_save_add_member(self):
        self.driver.find_element(By.XPATH, self.span_save_xpath).click()

    def set_search(self, name):
        self.driver.find_element(By.XPATH, self.input_search_xpath).send_keys(name)

    def click_search(self):
        self.driver.find_element(By.XPATH, self.span_search_xpath).click()

    def click_refresh(self):
        self.driver.find_element(By.XPATH, self.button_refresh_xpath).click()
