from locators.common_locators import CommonLocators
from locators.recipes_locators import RecipesPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class RecipesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RecipesPageLocators()
        self.locator = CommonLocators()

    def click_recipies(self):
        self.click_element("hyperlink_recipies_xpath", self.locators.hyperlink_recipies_xpath)

    def click_add_recipies(self):
        self.click_element("button_add_recipies_xpath", self.locators.button_add_recipies_xpath)

    def set_name(self, name):
        self.send_keys_to_element(name, "input_name_xpath", self.locators.input_name_xpath)

    def set_description(self, desc):
        self.send_keys_to_element(desc, "textarea_description_xpath", self.locators.textarea_description_xpath)

    def choose_image(self):
        self.perform_click_and_image_upload("span_choose_image_xpath", self.locators.span_choose_image_xpath,
                                            self.locators.upload_image)

    def select_audio(self, audio_path):
        self.send_keys_to_element(audio_path, "input_audio_xpath", self.locators.input_audio_xpath)

    def click_save(self):
        self.click_element("span_save_xpath", self.locators.span_save_xpath)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_ok_xpath", self.locators.span_ok_xpath)

    def click_edit(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        sleep(SHORT_WAIT)
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)

    def edit_image(self):
        self.perform_click_and_image_upload("span_choose_image_xpath", self.locators.span_choose_image_xpath,
                                            self.locators.edit_upload_image)

    def search_recipies(self, name):
        self.send_keys_to_element(name, "input_search_xpath", self.locators.input_search_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def add_new_recipe(self, name, desc, video_path):
        self.click_add_recipies()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_description(desc)
        sleep(SHORT_WAIT)
        self.choose_image()
        sleep(MEDIUM_WAIT)
        self.select_audio(video_path)
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_recipe(self):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.edit_image()
        sleep(SHORT_WAIT)
        self.click_save()

    def search_recipes(self, search_recipe):
        self.search_recipies(search_recipe)
        sleep(SHORT_WAIT)
        self.click_refresh()

    def negative_testing_add_recipes_without_fill_any_field(self):
        self.click_add_recipies()
        sleep(SHORT_WAIT)
        self.click_save()

    def negative_testing_add_recipes_only_fill_name(self, name):
        self.click_add_recipies()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.click_save()

    def negative_testing_add_recipes_only_add_audio(self, video_path):
        self.click_add_recipies()
        sleep(SHORT_WAIT)
        self.select_audio(video_path)
        sleep(SHORT_WAIT)
        self.click_save()
        sleep(SHORT_WAIT)

    def negative_testing_add_recipes_add_spaces_for_name(self, name, description, video_path):
        self.click_add_recipies()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.choose_image()
        sleep(SHORT_WAIT)
        self.select_audio(video_path)
        sleep(SHORT_WAIT)
        self.click_save()

    def negative_testing_add_recipes_only_add_name_and_description(self, name, description):
        self.click_add_recipies()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_description(description)

    def negative_testing_add_recipes_without_add_audio(self, name, description):
        self.click_add_recipies()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.choose_image()
        sleep(SHORT_WAIT)
        self.click_save()
