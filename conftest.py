import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome")
    parser.addoption('--language', action='store', default='ru',
                     help="ru, en, etc...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    if browser_name == "chrome" and user_language:
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome")
    yield browser
    #time.sleep(10)
    print("\nquit browser..")
    browser.quit()
