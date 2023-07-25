import time
from selenium.webdriver.common.by import By


class UserPage:
    span_user_xpath = "//span[normalize-space()='User']"
    hyperlink_userManagement_xpath = "//a[normalize-space()='User Management']"
    hyperlink_userRole_xpath = "//a[normalize-space()='User Role']"
    button_addUserRole_xpath = "//button[@class='ant-btn d-flex align-items-center " \
                               "ant-btn-primary ng-star-inserted']"
    input_role_xpath = "//input[@id='role-name']"
    permission_xpath = "//*[@id='userForm']/div[2]/nz-form-item/nz-form-control"
    div_userManagement_xpath = "//div[normalize-space()='User Management']"
    div_recipies_xpath = "//div[normalize-space()='Recipes']"
    div_eyeDonations_xpath = "//div[normalize-space()='EyeDonations']"
    div_banners_xpath = "//div[normalize-space()='Banners']"
    div_body_xpath = "(//div[@class='ant-drawer-body'])[1]"
    button_save_xpath = "//button[@type='submit']"
    button_edit_xpath = "/html/body/blind-app-root/blind-app-layout/nz-layout/nz-layout/nz-content/div[" \
                        "2]/blind-app-roles/div/div/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table" \
                        "/tbody/tr[2]/td[2]/button"
    span_removeUserManagement_xpath = "(//span[@class='ant-select-selection-item-remove ng-star-inserted'])[1]"
    span_removeRecipies_xpath = "(//span[@class='ant-select-selection-item-remove ng-star-inserted'])[2]"
    span_addMember_xpath = "//span[contains(text(),'Add member')]"
    input_username_xpath = "//input[@id='username']"
    span_generatePassword_xpath = "//span[normalize-space()='Generate Password']"
    input_email_xpath = "//input[@id='email']"
    input_firstName_xpath = "//input[@id='f-name']"
    input_lastName_xpath = "//input[@id='l-name']"
    input_selectRole_xpath = "//*[@id='userForm']/div[6]/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top" \
                             "-control/nz-select-search/input"
    div_role_xpath = "//div[normalize-space()='Testing']"
    input_activeStatus_xpath = "//*[@id='userForm']/div[7]/nz-form-item/nz-form-control/div/div/nz-select/nz-select" \
                               "-top-control/nz-select-search/input"
    div_inactive_xpath = "//div[normalize-space()='Inactive']"
    span_save_xpath = "//span[normalize-space()='Save']"
    input_search_xpath = "//input[@placeholder='Search name']"
    span_search_xpath = "//span[@class='anticon anticon-search']"
    button_refresh_xpath = "(//button[@class='ant-btn d-flex align-items-center p-0 justify-content-center " \
                           "ng-star-inserted'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickUser(self):
        self.driver.find_element(By.XPATH, self.span_user_xpath).click()

    def clickUserManagement(self):
        self.driver.find_element(By.XPATH, self.hyperlink_userManagement_xpath).click()

    def clickUserRole(self):
        self.driver.find_element(By.XPATH, self.hyperlink_userRole_xpath).click()

    def clickAddUserRole(self):
        self.driver.find_element(By.XPATH, self.button_addUserRole_xpath).click()

    def setRole(self, role):
        self.driver.find_element(By.XPATH, self.input_role_xpath).send_keys(role)

    def clickPermission(self):
        self.driver.find_element(By.XPATH, self.permission_xpath).click()

    def clickPermission_UserManagement(self):
        self.driver.find_element(By.XPATH, self.div_userManagement_xpath).click()

    def clickPermission_Recipies(self):
        self.driver.find_element(By.XPATH, self.div_recipies_xpath).click()

    def clickPermission_EyeDonations(self):
        self.driver.find_element(By.XPATH, self.div_eyeDonations_xpath).click()

    def clickPermission_Banners(self):
        self.driver.find_element(By.XPATH, self.div_banners_xpath).click()

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def clickEdit(self):
        self.driver.find_element(By.XPATH, self.button_edit_xpath).click()

    def removePermission_UserManagement(self):
        self.driver.find_element(By.XPATH, self.span_removeUserManagement_xpath).click()

    def removePermission_Recipies(self):
        self.driver.find_element(By.XPATH, self.span_removeRecipies_xpath).click()

    def editRoleName(self, name):
        self.driver.find_element(By.XPATH, self.input_role_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.input_role_xpath).send_keys(name)

    def clickAddMember(self):
        self.driver.find_element(By.XPATH, self.span_addMember_xpath).click()

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.input_username_xpath).send_keys(username)

    def clickGeneratePassword(self):
        self.driver.find_element(By.XPATH, self.span_generatePassword_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.input_firstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.input_lastName_xpath).send_keys(lastname)

    def clickRole(self):
        self.driver.find_element(By.XPATH, self.input_selectRole_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.div_role_xpath).click()

    def clickActiveStatus(self):
        self.ActiveStatus = self.driver.find_element(By.XPATH, self.input_activeStatus_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.ActiveStatus)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.div_inactive_xpath).click()

    def clickSave_addMember(self):
        self.driver.find_element(By.XPATH, self.span_save_xpath).click()

    def setSearch(self, name):
        self.driver.find_element(By.XPATH, self.input_search_xpath).send_keys(name)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.span_search_xpath).click()

    def clickRefresh(self):
        self.driver.find_element(By.XPATH, self.button_refresh_xpath).click()
