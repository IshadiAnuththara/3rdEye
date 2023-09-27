from locators.common_locators import CommonLocators
from locators.user_locators import UsersPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class UserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = UsersPageLocators()
        self.locator = CommonLocators()

    def click_user(self):
        self.click_element("span_user_xpath", self.locators.span_user_xpath)

    def click_user_management(self):
        self.click_element("hyperlink_user_management_xpath", self.locators.hyperlink_user_management_xpath)

    def click_user_role(self):
        self.click_element("hyperlink_user_role_xpath", self.locators.hyperlink_user_role_xpath)

    def click_add_user_role(self):
        self.click_element("button_add_user_role_xpath", self.locators.button_add_user_role_xpath)

    def set_role(self, role):
        self.send_keys_to_element(role, "input_role_xpath", self.locators.input_role_xpath)

    def click_permission(self):
        self.click_element("permission_xpath", self.locators.permission_xpath)

    def click_permission_user_management(self):
        self.click_element("div_user_management_xpath", self.locators.div_user_management_xpath)

    def click_permission_recipies(self):
        self.click_element("div_recipies_xpath", self.locators.div_recipies_xpath)

    def click_permission_eye_donations(self):
        self.click_element("div_eye_donations_xpath", self.locators.div_eye_donations_xpath)

    def click_permission_banners(self):
        self.click_element("div_banners_xpath", self.locators.div_banners_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_edit(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)

    def remove_permission_user_management(self):
        self.click_element("span_remove_user_management_xpath",
                           self.locators.span_remove_user_management_xpath)

    def remove_permission_recipies(self):
        self.click_element("span_remove_recipies_xpath", self.locators.span_remove_recipies_xpath)

    def edit_role_name(self, name):
        self.clear_fields("input_role_xpath", self.locators.input_role_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(name, "input_role_xpath", self.locators.input_role_xpath)

    def click_add_member(self):
        self.click_element("span_add_member_xpath", self.locators.span_add_member_xpath)

    def set_username(self, username):
        self.send_keys_to_element(username, "input_username_xpath", self.locators.input_username_xpath)

    def click_generate_password(self):
        self.click_element("span_generate_password_xpath", self.locators.span_generate_password_xpath)

    def set_email(self, email):
        self.send_keys_to_element(email, "input_email_xpath", self.locators.input_email_xpath)

    def set_first_name(self, firstname):
        self.send_keys_to_element(firstname, "input_first_name_xpath",
                                  self.locators.input_first_name_xpath)

    def set_last_name(self, lastname):
        self.send_keys_to_element(lastname, "input_last_name_xpath", self.locators.input_last_name_xpath)

    def click_role(self):
        self.click_element("input_select_role_xpath", self.locators.input_select_role_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_role_xpath", self.locators.div_role_xpath)

    def click_active_status(self):
        active_status = self.find_element("input_active_status_xpath", self.locators.input_active_status_xpath)
        sleep(SHORT_WAIT)
        self.driver.execute_script("arguments[0].click();", active_status)
        sleep(SHORT_WAIT)
        self.click_element("div_inactive_xpath", self.locators.div_inactive_xpath)

    def click_save_add_member(self):
        self.click_element("span_save_xpath", self.locators.span_save_xpath)

    def set_search(self, name):
        self.send_keys_to_element(name, "input_search_xpath", self.locators.input_search_xpath)

    def click_search(self):
        self.click_element("span_search_xpath", self.locators.span_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def add_member(self, name, email, first_name, last_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_username(name)
        sleep(SHORT_WAIT)
        self.click_generate_password()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_first_name(first_name)
        sleep(SHORT_WAIT)
        self.set_last_name(last_name)
        sleep(SHORT_WAIT)
        self.click_role()
        sleep(SHORT_WAIT)
        self.click_active_status()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def search_member(self, search_name):
        self.set_search(search_name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()

    def negative_testing_add_member_without_filling_any_field(self):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_only_add_email(self, email):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_only_add_email_first_name_last_name(self, email, first_name, last_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_first_name(first_name)
        sleep(SHORT_WAIT)
        self.set_last_name(last_name)
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_only_add_first_name(self, first_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_first_name(first_name)
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_only_add_last_name(self, last_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_last_name(last_name)
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_add_invalid_email(self, username, email, first_name, last_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_username(username)
        sleep(SHORT_WAIT)
        self.click_generate_password()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_first_name(first_name)
        sleep(SHORT_WAIT)
        self.set_last_name(last_name)
        sleep(SHORT_WAIT)
        self.click_role()
        sleep(SHORT_WAIT)
        self.click_active_status()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_add_existing_user(self, username, email, first_name, last_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_username(username)
        sleep(SHORT_WAIT)
        self.click_generate_password()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_first_name(first_name)
        sleep(SHORT_WAIT)
        self.set_last_name(last_name)
        sleep(SHORT_WAIT)
        self.click_role()
        sleep(SHORT_WAIT)
        self.click_active_status()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_add_existing_email(self, username, email, first_name, last_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_username(username)
        sleep(SHORT_WAIT)
        self.click_generate_password()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_first_name(first_name)
        sleep(SHORT_WAIT)
        self.set_last_name(last_name)
        sleep(SHORT_WAIT)
        self.click_role()
        sleep(SHORT_WAIT)
        self.click_active_status()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_without_select_role_and_active_status(self, username, email, first_name, last_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_username(username)
        sleep(SHORT_WAIT)
        self.click_generate_password()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_first_name(first_name)
        sleep(SHORT_WAIT)
        self.set_last_name(last_name)
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_without_select_active_status(self, username, email, first_name, last_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_username(username)
        sleep(SHORT_WAIT)
        self.click_generate_password()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_first_name(first_name)
        sleep(SHORT_WAIT)
        self.set_last_name(last_name)
        sleep(SHORT_WAIT)
        self.click_role()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_only_select_role(self):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.click_role()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_only_add_password(self):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.click_generate_password()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_only_add_username(self, username):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_username(username)
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_only_add_user_name_and_password(self, username):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_username(username)
        sleep(SHORT_WAIT)
        self.click_generate_password()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def negative_testing_add_member_only_select_active_status(self):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.click_active_status()
        sleep(SHORT_WAIT)
        self.click_save_add_member()

    def add_new_user_role(self, role):
        self.click_add_user_role()
        sleep(SHORT_WAIT)
        self.set_role(role)
        sleep(SHORT_WAIT)
        self.click_permission()
        sleep(SHORT_WAIT)
        self.click_permission_user_management()
        sleep(SHORT_WAIT)
        self.click_permission_recipies()
        sleep(SHORT_WAIT)
        self.click_permission_eye_donations()
        sleep(SHORT_WAIT)
        self.click_permission_banners()
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_user_role(self, role_name):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.edit_role_name(role_name)
        sleep(SHORT_WAIT)
        self.remove_permission_user_management()
        sleep(SHORT_WAIT)
        self.remove_permission_recipies()
        sleep(SHORT_WAIT)
        self.click_save()

    def negative_testing_add_user_role_without_enter_any_field(self):
        self.click_add_user_role()
        sleep(SHORT_WAIT)
        self.click_save()

    def negative_testing_add_user_role_only_add_user_role(self, role):
        self.click_add_user_role()
        sleep(SHORT_WAIT)
        self.set_role(role)
        sleep(SHORT_WAIT)
        self.click_save()

    def negative_testing_add_user_role_only_add_permissions(self):
        self.click_add_user_role()
        sleep(SHORT_WAIT)
        self.click_permission()
        sleep(SHORT_WAIT)
        self.click_permission_user_management()
        sleep(SHORT_WAIT)
        self.click_permission_recipies()
        sleep(SHORT_WAIT)
        self.click_permission_eye_donations()
        sleep(SHORT_WAIT)
        self.click_permission_banners()
        sleep(SHORT_WAIT)
        self.click_save()

    def negative_testing_add_user_role_existing_user_role(self, role):
        self.click_add_user_role()
        sleep(SHORT_WAIT)
        self.set_role(role)
        sleep(SHORT_WAIT)
        self.click_permission()
        sleep(SHORT_WAIT)
        self.click_permission_user_management()
        sleep(SHORT_WAIT)
        self.click_permission_recipies()
        sleep(SHORT_WAIT)
        self.click_permission_eye_donations()
        sleep(SHORT_WAIT)
        self.click_permission_banners()
        sleep(SHORT_WAIT)
        self.click_save()
