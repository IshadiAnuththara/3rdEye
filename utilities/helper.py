import os


def take_screenshot(driver, folder, filename):
    screenshot_path = os.path.join(folder, filename)
    driver.save_screenshot(screenshot_path)
    return screenshot_path

# def perform_login_with_invalid_credentials_assertion(driver, login_page, logger, success_message, unique_message):
#     if success_message in login_page.retrieve_warning_message():
#         assert True
#         logger.info(f"********* {unique_message} - Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\screenshots\\", f"{unique_message}_scr.png")
#         logger.error(f"********* {unique_message} - Test Failed *********")
#         assert False
#
#
# def perform_create_game_negative_testing_assertion(driver, game_page, logger, success_message, unique_message):
#     if success_message in game_page.retrieve_warning_message():
#         assert True
#         logger.info(f"********* {unique_message} - Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\screenshots\\", f"{unique_message}_scr.png")
#         logger.error(f"********* {unique_message} - Test Failed *********")
#         assert False

