import time
import pyautogui
from utilities.helper import take_screenshot

SHORT_WAIT = 4
MEDIUM_WAIT = 8
LONG_WAIT = 10


def sleep(seconds):
    time.sleep(seconds)


def upload_image(image_path):
    sleep(SHORT_WAIT)
    pyautogui.typewrite(image_path)
    pyautogui.press("enter")
    sleep(SHORT_WAIT)


def upload_video(video_path):
    sleep(SHORT_WAIT)
    pyautogui.typewrite(video_path)
    pyautogui.press("enter")
    sleep(SHORT_WAIT)


# Login Assertions
def perform_login_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_warning_message():
        assert True
        logger.info("********* Login Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_login_scr.png")
        logger.error("*********  Login Test Failed *********")
        assert False


def perform_login_invalid_credentials_001_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_warning_message():
        assert True
        logger.info("********* Login with valid username and invalid password - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_login_with_valid_username_and_invalid_password_scr.png")
        logger.error("********* Login with valid username and invalid password - Test Failed *********")
        assert False


def perform_login_invalid_credentials_002_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_warning_message():
        assert True
        logger.info("********* Login with invalid username and valid password - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_login_with_invalid_username_and_valid_password_scr.png")
        logger.error("********* Login with invalid username and valid password - Test Failed *********")
        assert False


def perform_login_invalid_credentials_003_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_warning_message():
        assert True
        logger.info("********* Login with invalid username and invalid password - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_login_with_invalid_username_and_invalid_password_scr.png")
        logger.error("********* Login with invalid username and invalid password - Test Failed *********")
        assert False


def perform_login_invalid_credentials_004_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_warning_message():
        assert True
        logger.info("********* Login without username and password - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_login_without_enter_username_password_scr.png")
        logger.error("********* Login without username and password - Test Failed *********")
        assert False


def perform_add_new_banner_assertion(driver, banners_page, logger, success_message):
    if success_message in banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Banner - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_banners_scr.png")
        logger.error("********* Add Banner -  - Test Failed *********")
        assert False


def perform_close_banners_assertion(driver, banners_page, logger, success_message):
    if success_message in banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Close banners - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_close_banners_scr.png")
        logger.error("********* Close banners -  - Test Failed *********")
        assert False


def perform_edit_banners_assertion(driver, banners_page, logger, success_message):
    if success_message in banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit banners - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_banners_scr.png")
        logger.error("********* Edit banners -  - Test Failed *********")
        assert False


def perform_show_banners_assertion(driver, banners_page, logger, success_message):
    if success_message in banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Show Banners - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_show_banners_scr.png")
        logger.error("********* Show Banners -  - Test Failed *********")
        assert False


def perform_delete_banners_assertion(driver, banners_page, logger, success_message):
    if success_message in banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Banners - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_banners_scr.png")
        logger.error("********* Delete Banners -  - Test Failed *********")
        assert False


def perform_delete_eye_donations_assertion(driver, eye_donation_page, logger, success_message):
    if success_message in eye_donation_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Eye Donation - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_eye_donation_scr.png")
        logger.error("********* Delete Eye Donation - Test Failed *********")
        assert False


def perform_add_new_recipe_assertion(driver, recipe_page, logger, success_message):
    if success_message in recipe_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Recipes - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_new_recipe_scr.png")
        logger.error("********* Add Recipes - Test Failed *********")
        assert False


def perform_edit_recipe_assertion(driver, recipe_page, logger, success_message):
    if success_message in recipe_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Recipes - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_recipe_scr.png")
        logger.error("********* Edit Recipes - Test Failed *********")
        assert False


def perform_delete_recipe_assertion(driver, recipe_page, logger, success_message):
    if success_message in recipe_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Recipes - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_recipe_scr.png")
        logger.error("********* Delete Recipes - Test Failed *********")
        assert False


def perform_add_recipes_without_fill_any_field_assertion(driver, recipe_page, logger, success_message):
    if success_message in recipe_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Recipes - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_recipes_negative_testing_001_scr.png")
        logger.error("********* Add Recipes - Test Failed *********")
        assert False


def perform_add_recipes_only_fill_name_assertion(driver, recipe_page, logger, success_message):
    if success_message in recipe_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Recipes - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_recipes_negative_testing_002_scr.png")
        logger.error("********* Add Recipes - Test Failed *********")
        assert False


def perform_add_recipes_only_add_audio_assertion(driver, recipe_page, logger, success_message):
    if success_message in recipe_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Recipes - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_recipes_negative_testing_003_scr.png")
        logger.error("********* Add Recipes - Test Failed *********")
        assert False


def perform_add_recipes_add_spaces_for_name_assertion(driver, recipe_page, logger, success_message):
    if success_message in recipe_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Recipes - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_recipes_negative_testing_004_scr.png")
        logger.error("********* Add Recipes - Test Failed *********")
        assert False


def perform_add_recipes_only_add_name_and_description_assertion(driver, recipe_page, logger, success_message):
    if success_message in recipe_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Recipes - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_recipes_negative_testing_005_scr.png")
        logger.error("********* Add Recipes - Test Failed *********")
        assert False


def perform_add_recipes_without_add_audio_assertion(driver, recipe_page, logger, success_message):
    if success_message in recipe_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Recipes - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_recipes_negative_testing_006_scr.png")
        logger.error("********* Add Recipes - Test Failed *********")
        assert False


def perform_add_member_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_without_filling_any_field_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_001_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_only_add_email_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_002_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_only_add_email_first_name_last_name_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_003_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_only_add_first_name_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_only_add_last_name_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_add_invalid_email_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_add_existing_user_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_add_existing_email_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_without_select_role_and_active_status_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_without_select_active_status_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_only_select_role_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_only_add_password_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_only_add_username_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_member_only_select_active_status_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add Member - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_member_negative_testing_004_scr.png")
        logger.error("********* Add Member - Test Failed *********")
        assert False


def perform_add_new_user_role_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add user role - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_new_user_role_scr.png")
        logger.error("********* Add user role - Test Failed *********")
        assert False


def perform_edit_user_role_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit user role - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_user_role_scr.png")
        logger.error("********* Edit user role - Test Failed *********")
        assert False


def perform_add_user_role_without_enter_any_field_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add user role - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_user_role_negative_testing_001_scr.png")
        logger.error("********* Add user role - Test Failed *********")
        assert False


def perform_add_user_role_only_add_user_role_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add user role - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_user_role_negative_testing_002_scr.png")
        logger.error("********* Add user role - Test Failed *********")
        assert False


def perform_add_user_role_only_add_permissions_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add user role - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_user_role_negative_testing_003_scr.png")
        logger.error("********* Add user role - Test Failed *********")
        assert False


def perform_add_user_role_existing_user_role_assertion(driver, user_page, logger, success_message):
    if success_message in user_page.retrieve_warning_message():
        assert True
        logger.info("********* Add user role - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_user_role_negative_testing_003_scr.png")
        logger.error("********* Add user role - Test Failed *********")
        assert False


def perform_logout_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_warning_message():
        assert True
        logger.info("********* Logout -  Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_logout_scr.png")
        logger.error("********* Logout -  Test Failed *********")
        assert False


# Announcements Assertion
def perform_create_announcement_assertion(driver, announcement_page, logger, success_message):
    if success_message in announcement_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Announcement Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_announcement_scr.png")
        logger.error("*********  Create Announcement Test Failed *********")
        assert False


def perform_edit_announcement_assertion(driver, announcement_page, logger, success_message):
    if success_message in announcement_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit announcement Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_announcement_scr.png")
        logger.error("********* Edit announcement Test Failed *********")
        assert False


def perform_delete_announcement_assertion(driver, announcement_page, logger, success_message):
    if success_message in announcement_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete announcement Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_announcement_scr.png")
        logger.error("********* Delete announcement Test Failed *********")
        assert False


# Campaign Assertions
def perform_create_campaign_assertion(driver, campaign_page, logger, success_message):
    if success_message in campaign_page.retrieve_warning_message():
        assert True
        logger.info("********* Create campaign Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_campaign_scr.png")
        logger.error("*********  Create campaign Test Failed *********")
        assert False


def perform_edit_campaign_assertion(driver, campaign_page, logger, success_message):
    if success_message in campaign_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit campaign Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_campaign_scr.png")
        logger.error("********* Edit campaign Test Failed *********")
        assert False


def perform_delete_campaign_assertion(driver, campaign_page, logger, success_message):
    if success_message in campaign_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete campaign Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_campaign_scr.png")
        logger.error("********* Delete campaign Test Failed *********")
        assert False


# Complains Assertions
def perform_ignore_complains_assertion(driver, complain_page, logger, success_message):
    if success_message in complain_page.retrieve_warning_message():
        assert True
        logger.info("********* Ignore complains Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_ignore_complains_scr.png")
        logger.error("********* Ignore Complains Test Failed *********")
        assert False


# Game Assertions
def perform_create_game_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new game Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_game_scr.png")
        logger.error("********* Create new game Test Failed *********")
        assert False


def perform_edit_game_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit game Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_game_scr.png")
        logger.error("********* Edit game Test Failed *********")
        assert False


def perform_delete_game_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete game Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_game_scr.png")
        logger.error("********* Delete game Test Failed *********")
        assert False


def perform_game_settings_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit setting Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_setting_scr.png")
        logger.error("********* Edit setting Test Failed *********")
        assert False


# Items Assertions
def perform_add_new_item_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Add new item Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_new_item_scr.png")
        logger.error("********* Add new item Test Failed *********")
        assert False


def perform_edit_item_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit item Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_item_scr.png")
        logger.error("********* Edit item Test Failed *********")
        assert False


def perform_delete_item_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete item Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_item_scr.png")
        logger.error("********* Delete item Test Failed *********")
        assert False


# Category Assertions
def perform_create_category_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Add new category Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_new_category_scr.png")
        logger.error("********* Add new category Test Failed *********")
        assert False


def perform_edit_category_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit category Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_category_scr.png")
        logger.error("********* Edit category Test Failed *********")
        assert False


# Scheduler Assertions
def perform_create_scheduler_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_schedule_scr.png")
        logger.error("********* Create new schedule Test Failed *********")
        assert False


def perform_edit_scheduler_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_schedule_scr.png")
        logger.error("********* Edit schedule Test Failed *********")
        assert False


def perform_delete_scheduler_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_schedule_scr.png")
        logger.error("********* Delete schedule Test Failed *********")
        assert False


# Item Schedule - Negative Testing Assertion
def perform_create_scheduler_negative_testing_001_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Scheduler - Without Enter Any Field - Negative Testing - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_schedule_negative_test_001_scr.png")
        logger.error("********* Create Scheduler - Without Enter Any Field - Negative Testing - Test Failed *********")
        assert False


def perform_create_scheduler_negative_testing_002_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Scheduler - Only Enter Item Name - Negative Testing - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_schedule_negative_test_002_scr.png")
        logger.error("********* Create Scheduler - Only Enter Item Name - Negative Testing - Test Failed *********")
        assert False


def perform_create_scheduler_negative_testing_003_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Scheduler - Without Enter End Time - Negative Testing - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_schedule_negative_test_003_scr.png")
        logger.error("********* Create Scheduler - Without Enter End Time - Negative Testing - Test Failed *********")
        assert False


def perform_create_scheduler_negative_testing_004_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Schedule - Item Quantity Exceed - Negative Testing - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_schedule_negative_test_004_scr.png")
        logger.error("********* Create Schedule - Item Quantity Exceed - Negative Testing - Test Failed *********")
        assert False


# Order and Shipping Assertions
def perform_edit_orders_assertion(driver, order_page, logger, success_message):
    if success_message in order_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit orders Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_orders_scr.png")
        logger.error("********* Edit orders Test Failed *********")
        assert False


# Brand Page Assertions
def perform_edit_brand_pages_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Brand pages Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_brand_pages_scr.png")
        logger.error("********* Edit Brand pages Test Failed *********")
        assert False


# Popup banners Assertions
def perform_create_popup_banners_assertion(driver, popup_banners_page, logger, success_message):
    if success_message in popup_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Pop-up Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_popup_banners_scr.png")
        logger.error("********* Create Pop-up Banners Test Failed *********")
        assert False


def perform_edit_popup_banners_assertion(driver, popup_banners_page, logger, success_message):
    if success_message in popup_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Pop-up Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_popup_banners_scr.png")
        logger.error("********* Edit Pop-up Banners Test Failed *********")
        assert False


def perform_delete_popup_banners_assertion(driver, popup_banners_page, logger, success_message):
    if success_message in popup_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Pop-up Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_popup_banners_scr.png")
        logger.error("********* Delete Pop-up Banners Test Failed *********")
        assert False


# Push Notifications Assertions
def perform_create_push_notifications_assertion(driver, push_notifications_page, logger, success_message):
    if success_message in push_notifications_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Push Notifications Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_push_notifications_scr.png")
        logger.error("********* Create Push Notifications Test Failed *********")
        assert False


def perform_edit_push_notifications_assertion(driver, push_notifications_page, logger, success_message):
    if success_message in push_notifications_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Push Notifications Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_push_notifications_scr.png")
        logger.error("********* Edit Push Notifications Test Failed *********")
        assert False


def perform_resend_push_notifications_assertion(driver, push_notifications_page, logger, success_message):
    if success_message in push_notifications_page.retrieve_warning_message():
        assert True
        logger.info("********* Resend Notification Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_resend_notifications_scr.png")
        logger.error("********* Resend Notification Test Failed *********")
        assert False


def perform_delete_push_notifications_assertion(driver, push_notifications_page, logger, success_message):
    if success_message in push_notifications_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Notification Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_push_notifications_scr.png")
        logger.error("********* Delete Notification Test Failed *********")
        assert False


# Player Management Assertions
def perform_edit_player_block_status_block_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit player Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_player_scr.png")
        logger.error("********* Edit player Test Failed *********")
        assert False


def perform_edit_player_block_status_unblock_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit player Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_player_scr.png")
        logger.error("********* Edit player Test Failed *********")
        assert False


def perform_edit_player_purchase_block_status_block_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit player Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_player_scr.png")
        logger.error("********* Edit player Test Failed *********")
        assert False


def perform_edit_player_purchase_block_status_unblock_assertion(driver, player_management_page, logger,
                                                                success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit player Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_player_scr.png")
        logger.error("********* Edit player Test Failed *********")
        assert False


# Quiz Assertions
def perform_create_quiz_assertion(driver, quiz_page, logger, success_message):
    if success_message in quiz_page.retrieve_warning_message():
        assert True
        logger.info("********* Create quiz Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_quiz_scr.png")
        logger.error("********* Create quiz Test Failed *********")
        assert False


def perform_edit_quiz_assertion(driver, quiz_page, logger, success_message):
    if success_message in quiz_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit quiz Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_quiz_scr.png")
        logger.error("********* Edit quiz Test Failed *********")
        assert False


def perform_delete_quiz_assertion(driver, quiz_page, logger, success_message):
    if success_message in quiz_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete quiz Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_quiz_scr.png")
        logger.error("********* Delete quiz Test Failed *********")
        assert False


def perform_create_new_quiz_category_assertion(driver, category_page, logger, success_message):
    if success_message in category_page.retrieve_warning_message():
        assert True
        logger.info("********* Create quiz category Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_quiz_category_scr.png")
        logger.error("********* Create quiz category Test Failed *********")
        assert False


def perform_edit_quiz_category_assertion(driver, category_page, logger, success_message):
    if success_message in category_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit quiz category Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_quiz_category_scr.png")
        logger.error("********* Edit quiz category Test Failed *********")
        assert False


def perform_create_new_quiz_schedule_assertion(driver, schedule_page, logger, success_message):
    if success_message in schedule_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new quiz schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_new_quiz_schedule_scr.png")
        logger.error("********* Create new quiz schedule Test Failed *********")
        assert False


def perform_edit_quiz_schedule_assertion(driver, schedule_page, logger, success_message):
    if success_message in schedule_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit quiz schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_quiz_schedule_scr.png")
        logger.error("********* Edit quiz schedule Test Failed *********")
        assert False


def perform_delete_quiz_schedule_assertion(driver, schedule_page, logger, success_message):
    if success_message in schedule_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete quiz schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_quiz_schedule_scr.png")
        logger.error("********* Delete quiz schedule Test Failed *********")
        assert False


# Support Message Assertions
def perform_reply_support_message_assertion(driver, player_support_page, logger, success_message):
    if success_message in player_support_page.retrieve_warning_message():
        assert True
        logger.info("********* player support Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_reply_support_message_scr.png")
        logger.error("********* player support Test Failed *********")
        assert False


# Store Banners Assertions
def perform_create_store_banners_assertion(driver, store_banners_page, logger, success_message):
    if success_message in store_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Store Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_store_banners_scr.png")
        logger.error("********* Create Store Banners Test Failed *********")
        assert False


def perform_delete_store_banners_assertion(driver, store_banners_page, logger, success_message):
    if success_message in store_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Store Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_store_banners_scr.png")
        logger.error("********* Delete Store Banners Test Failed *********")
        assert False


# Store Banners - Negative Testing Assertion
def perform_create_store_banners_negative_testing_001_assertion(driver, store_banners_page, logger, success_message):
    warning_message = store_banners_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create store banners - Without fill any field - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "store_banners_negative_testing_001_scr.png")
        logger.error("********* Create store banners - Without fill any field - Test Failed *********")
        assert False


def perform_create_store_banners_negative_testing_002_assertion(driver, store_banners_page, logger, success_message):
    warning_message = store_banners_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create store banners - Only add description - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "store_banners_negative_testing_002_scr.png")
        logger.error("********* Create store banners - Only add description - Test Failed *********")
        assert False


def perform_create_store_banners_negative_testing_003_assertion(driver, store_banners_page, logger, success_message):
    warning_message = store_banners_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create store banners - Only add image - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "store_banners_negative_testing_003_scr.png")
        logger.error("********* Create store banners - Only add image - Test Failed *********")
        assert False


def perform_create_store_banners_negative_testing_004_assertion(driver, store_banners_page, logger, success_message):
    warning_message = store_banners_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create store banners - Only fill redirect URL - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "store_banners_negative_testing_004_scr.png")
        logger.error("********* Create store banners - Only fill redirect URL - Test Failed *********")
        assert False


# Users Assertions
def perform_add_new_user_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Add New Member Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_new_member_scr.png")
        logger.error("********* Add New Member Test Failed Test Failed *********")
        assert False


def perform_update_user_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Member Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_member_scr.png")
        logger.error("********* Edit Member Test Failed *********")
        assert False


def perform_add_new_user_role_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Add User Role Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_new_user_role_scr.png")
        logger.error("********* Add User Role Test Failed *********")
        assert False


def perform_edit_user_role_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit User Role Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_user_role_scr.png")
        logger.error("********* Edit User Role Test Failed *********")
        assert False


def perform_remove_permissions_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Remove Permission Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_remove_permissions_scr.png")
        logger.error("********* Remove Permission Test Failed *********")
        assert False


def perform_create_new_email_domain_assertion(driver, settings_page, logger, success_message):
    if success_message in settings_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Email Domain Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_email_domain_scr.png")
        logger.error("********* Create Email Domain Test Failed *********")
        assert False


def perform_edit_email_domain_assertion(driver, settings_page, logger, success_message):
    if success_message in settings_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Email Domain Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_email_domain_scr.png")
        logger.error("********* Edit Email Domain Test Failed *********")
        assert False


def perform_delete_email_domain_assertion(driver, settings_page, logger, success_message):
    if success_message in settings_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Email Domain Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_email_domain_scr.png")
        logger.error("********* Delete Email Domain Test Failed *********")
        assert False


def perform_delete_player_posts_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete player posts Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_player_posts_scr.png")
        logger.error("********* Delete player posts Test Failed *********")
        assert False


def perform_update_settings_assertion(driver, settings_page, logger, success_message):
    if success_message in settings_page.retrieve_warning_message():
        assert True
        logger.info("********* Update Settings Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_update_settings_scr.png")
        logger.error("********* Update Settings Test Failed *********")
        assert False


# Popup banners - Negative Testing Assertion
def perform_create_popup_banners_negative_testing_001_assertion(driver, popup_banner_page, logger, success_message):
    warning_message = popup_banner_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create popup banners - without fill any field -  Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_popup_banners_negative_test_001_scr.png")
        logger.error("********* Create popup banners - without fill any field -  Test Failed *********")
        assert False


def perform_create_popup_banners_negative_testing_002_assertion(driver, popup_banner_page, logger, success_message):
    warning_message = popup_banner_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create popup banners - Only add image -  Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_popup_banners_negative_test_002_scr.png")
        logger.error("********* Create popup banners - Only add image -  Test Failed *********")
        assert False


def perform_create_popup_banners_negative_testing_003_assertion(driver, popup_banner_page, logger, success_message):
    warning_message = popup_banner_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create popup banners - Only add schedule end time -  Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_popup_banners_negative_test_003_scr.png")
        logger.error("********* Create popup banners - Only add schedule end time -  Test Failed *********")
        assert False


def perform_create_popup_banners_negative_testing_004_assertion(driver, popup_banner_page, logger, success_message):
    warning_message = popup_banner_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create popup banners - Only add schedule start time -  Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_popup_banners_negative_test_004_scr.png")
        logger.error("********* Create popup banners - Only add schedule start time -  Test Failed *********")
        assert False


def perform_create_popup_banners_negative_testing_005_assertion(driver, popup_banner_page, logger, success_message):
    warning_message = popup_banner_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create popup banners - Without set schedule end date -  Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_popup_banners_negative_test_005_scr.png")
        logger.error("********* Create popup banners - Without set schedule end date -  Test Failed *********")
        assert False


def perform_create_popup_banners_negative_testing_006_assertion(driver, popup_banner_page, logger, success_message):
    warning_message = popup_banner_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create popup banners - Without set schedule end date -  Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_popup_banners_negative_test_005_scr.png")
        logger.error("********* Create popup banners - Without set schedule end date -  Test Failed *********")
        assert False


# NEW UPDATES
def perform_assertion(driver, page, logger, success_message, function_name):
    if success_message in page.retrieve_warning_message():
        logger.info(f"********* Assertion for {function_name} Test Passed *********")
    else:
        logger.error(f"********* Assertion for {function_name} Test Failed *********")
        take_screenshot(driver, ".\\screenshots\\", f"{function_name.lower()}_scr.png")
        assert False


# Items - Negative Testing Assertion
def perform_add_item_negative_testing_001_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Add new item - Without Fill Any Field - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "add_item_negative_testing_001_scr.png")
        logger.error("********* Add new item - Without Fill Any Field - Test Failed *********")
        assert False


def perform_add_item_negative_testing_002_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Add new item - Only Enter Name - Category - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "add_item_negative_testing_002_scr.png")
        logger.error("********* Add new item - Only Enter Name - Category - Test Failed *********")
        assert False


def perform_add_item_negative_testing_003_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Add new item - Only Enter Name, Category & Description - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "add_item_negative_testing_003_scr.png")
        logger.error("********* Add new item - Only Enter Name, Category & Description - Test Failed *********")
        assert False


def perform_add_item_negative_testing_004_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Add new item - Only Fill Item Name - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "add_item_negative_testing_004_scr.png")
        logger.error("********* Add new item - Only Fill Item Name - Test Failed *********")
        assert False


def perform_add_item_negative_testing_005_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Add new item - Without Enter Category - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "add_item_negative_testing_005_scr.png")
        logger.error("********* Add new item - Without Enter Category - Test Failed *********")
        assert False


def perform_add_item_negative_testing_006_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Add new item - Without Enter Item Status - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "add_item_negative_testing_006_scr.png")
        logger.error("********* Add new item - Without Enter Item Status - Test Failed *********")
        assert False


def perform_add_item_negative_testing_007_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Add new item - Without Enter Pointz - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "add_item_negative_testing_007_scr.png")
        logger.error("********* Add new item - Without Enter Pointz - Test Failed *********")
        assert False


def perform_add_item_negative_testing_008_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Add new item -  Without Enter Stock - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "add_item_negative_testing_008_scr.png")
        logger.error("********* Add new item -  Without Enter Stock - Test Failed *********")
        assert False


def perform_delete_item_exist_event_negative_testing_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Delete Items - Exist event - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "delete_item_negative_testing_001_scr.png")
        logger.error("********* Delete Items - Exist event - Test Failed *********")
        assert False


def perform_add_existing_item_negative_testing_assertion(driver, item_page, logger, success_message):
    warning_message = item_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Add Item -  Existing - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "add_item_negative_testing_009_scr.png")
        logger.error("********* Add Item -  Existing - Test Failed *********")
        assert False


# Game - Negative Testing Assertion
def perform_create_game_negative_testing_001_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create a new game - Without Fill Any Field - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_001_scr.png")
        logger.error("********* Create a new game - Without Fill Any Field - Test Failed *********")
        assert False


def perform_create_game_negative_testing_002_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - Duplicate answers - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_002_scr.png")
        logger.error("********* Create New Game - Duplicate answers - Test Failed *********")
        assert False


def perform_create_game_negative_testing_003_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - Fill All Field - No Shuffle - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_003_scr.png")
        logger.error("********* Create New Game - Fill All Field - No Shuffle - Test Failed *********")
        assert False


def perform_create_game_negative_testing_004_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create a new game - Fill All Field - Not Add Answers - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_004_scr.png")
        logger.error("********* Create a new game - Fill All Field - Not Add Answers - Test Failed *********")
        assert False


def perform_create_game_negative_testing_005_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create a new game - Without Add Pointz - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_005_scr.png")
        logger.error("********* Create a new game - Without Add Pointz - Test Failed *********")
        assert False


def perform_create_game_negative_testing_006_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create a new game - Without Enter Minus Pointz - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_006_scr.png")
        logger.error("********* Create a new game - Without Enter Minus Pointz - Test Failed *********")
        assert False


def perform_create_game_negative_testing_007_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create a new game - Without Enter Plus Pointz - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_007_scr.png")
        logger.error("********* Create a new game - Without Enter Plus Pointz - Test Failed *********")
        assert False


def perform_create_game_negative_testing_008_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create a new game - Without Select Game Level - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_008_scr.png")
        logger.error("********* Create a new game - Without Select Game Level - Test Failed *********")
        assert False


def perform_create_game_negative_testing_009_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create a new game - Without Select Status - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_009_scr.png")
        logger.error("********* Create a new game - Without Select Status - Test Failed *********")
        assert False


def perform_create_game_negative_testing_010_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - Enter Numbers - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_010_scr.png")
        logger.error("********* Create New Game - Enter Numbers - Test Failed *********")
        assert False


def perform_create_game_negative_testing_011_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - Enter Symbols - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_011_scr.png")
        logger.error("********* Create New Game - Enter Symbols - Test Failed *********")
        assert False


def perform_create_game_negative_testing_012_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - Only Fill Word, Level, Minus Pointz and Shuffle -"
                    " Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_012_scr.png")
        logger.error("********* Create New Game - Only Fill Word, Level, Minus Pointz and Shuffle -"
                     " Test Failed *********")
        assert False


def perform_create_game_negative_testing_013_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - Only Fill Word Level, Plus Pointz & Shuffle - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_013_scr.png")
        logger.error("********* Create New Game - Only Fill Word Level, Plus Pointz & Shuffle - Test Failed *********")
        assert False


def perform_create_game_negative_testing_014_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - Only Fill Word Level & Shuffle - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_014_scr.png")
        logger.error("********* Create New Game - Only Fill Word Level & Shuffle - Test Failed *********")
        assert False


def perform_create_game_negative_testing_015_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - only fill word and no shuffle - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_015_scr.png")
        logger.error("********* Create New Game - only fill word and no shuffle - Test Failed *********")
        assert False


def perform_create_game_negative_testing_016_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - only fill word and shuffle - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_016_scr.png")
        logger.error("********* Create New Game - only fill word and shuffle - Test Failed *********")
        assert False


def perform_create_game_negative_testing_017_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - only fill word and no shuffle- Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_017_scr.png")
        logger.error("********* Create New Game - only fill word and no shuffle - Test Failed *********")
        assert False


def perform_create_game_negative_testing_018_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create a game - Exist game - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_018_scr.png")
        logger.error("********* Create a game - Exist game - Test Failed *********")
        assert False


def perform_create_edit_answered_game_negative_testing_001_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create New Game - only fill word and no shuffle - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_017_scr.png")
        logger.error("********* Create New Game - only fill word and no shuffle - Test Failed *********")
        assert False


# Quiz - Negative Testing Assertion
def perform_create_quizzes_negative_testing_001_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Without fill any field - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_001_scr.png")
        logger.error("********* Create quiz - Without fill any field - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_002_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Only add answers - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_002_scr.png")
        logger.error("********* Create quiz - Only add answers - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_003_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Only add wrong answers - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_003_scr.png")
        logger.error("********* Create quiz - Only add wrong answers - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_004_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Only enter category - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_004_scr.png")
        logger.error("********* Create quiz - Only enter category - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_005_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Only enter description - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_005_scr.png")
        logger.error("********* Create quiz - Only enter description - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_006_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Only enter minus points - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_006_scr.png")
        logger.error("********* Create quiz - Only enter minus points - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_007_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Only enter plus points - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_007_scr.png")
        logger.error("********* Create quiz - Only enter plus points - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_008_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Only enter quiz name - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_008_scr.png")
        logger.error("********* Create quiz - Only enter quiz name - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_009_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Only select quiz level - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_009_scr.png")
        logger.error("********* Create quiz - Only select quiz level - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_010_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Without enter description - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_010_scr.png")
        logger.error("********* Create quiz - Without enter description - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_011_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Without select approval - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_011_scr.png")
        logger.error("********* Create quiz - Without select approval - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_012_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Without select quiz level - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_012_scr.png")
        logger.error("********* Create quiz - Without select quiz level - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_013_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Without select quiz category - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_013_scr.png")
        logger.error("********* Create quiz - Without select quiz category - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_014_assertion(driver, quiz_page, logger, success_message):
    warning_message = quiz_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz - Existing_quiz - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "create_quiz_negative_testing_014_scr.png")
        logger.error("********* Create quiz - Existing_quiz - Test Failed *********")
        assert False


# Quiz category - Negative Testing Assertion
def perform_create_quiz_categories_negative_testing_001_assertion(driver, categories_page, logger, success_message):
    warning_message = categories_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz category - Without fill category name - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "quiz_category_negative_testing_001_scr.png")
        logger.error("********* Create quiz category - Without fill category name - Test Failed *********")
        assert False


def perform_create_quiz_categories_negative_testing_002_assertion(driver, categories_page, logger, success_message):
    warning_message = categories_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz category - Enter exist category - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "quiz_category_negative_testing_002_scr.png")
        logger.error("********* Create quiz category - Enter exist category - Test Failed *********")
        assert False


# Quiz Schedule - Negative Testing Assertion
def perform_create_quiz_schedule_negative_testing_001_assertion(driver, schedule_page, logger, success_message):
    warning_message = schedule_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz schedule - Without fill any field - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "quiz_schedule_negative_testing_001_scr.png")
        logger.error("********* Create quiz schedule - Without fill any field - Test Failed *********")
        assert False


def perform_create_quiz_schedule_negative_testing_002_assertion(driver, schedule_page, logger, success_message):
    warning_message = schedule_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz schedule - Only enter quiz category - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "quiz_schedule_negative_testing_002_scr.png")
        logger.error("********* Create quiz schedule - Only enter quiz category - Test Failed *********")
        assert False


def perform_create_quiz_schedule_negative_testing_003_assertion(driver, schedule_page, logger, success_message):
    warning_message = schedule_page.retrieve_warning_message()
    logger.debug(f"Warning Message on Page: {warning_message}")
    if success_message in warning_message:
        assert True
        logger.info("********* Create quiz schedule - Without enter start time - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "quiz_schedule_negative_testing_003_scr.png")
        logger.error("********* Create quiz schedule - Without enter start time - Test Failed *********")
        assert False
