import self
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
    # config._metadata['Project Name'] = 'playpointz backend'
    # config._metadata['Module Name'] = 'Login'
    # config._metadata['Tester'] = 'Ishadi Rathnayake'



