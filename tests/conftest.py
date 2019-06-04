import pytest
from base.webdriverFactory import WebDriverFactory
from pages.webpages.login.login_page import LoginPage

@pytest.fixture(scope="class")
def setUp(request, browser, os):
    print("Running setUp")
    wdf = WebDriverFactory(browser, os)
    items = wdf.getWebDriverInstance()
    driver = items[0]
    browser = items[1]
    os = items[2]
    thisdir = items[3]

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.browser = browser
        request.cls.os = os
        request.cls.thisdir = thisdir
        request.cls.WebDriverFactory = WebDriverFactory(browser, os)

    yield driver, browser, os, thisdir

    driver.quit()
    print("Running tearDown")

@pytest.fixture(scope="class")
def loginWithSetUp(request, browser, os):
    print("Running login along with setup")
    wdf = WebDriverFactory(browser, os)
    items = wdf.getWebDriverInstance()
    driver = items[0]
    browser = items[1]
    os = items[2]
    thisdir = items[3]

    lp = LoginPage(driver)
    lp.firstlogin("sqatester2018@gmail.com", "Automation123#", "AUTOMATION TESTER")

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.browser = browser
        request.cls.os = os
        request.cls.thisdir = thisdir
        request.cls.WebDriverFactory = WebDriverFactory(browser, os)

    yield driver, browser, os, thisdir

    driver.quit()
    print("Running tearDown from login with setup")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    return browser

@pytest.fixture(scope="session")
def os(request):
    os = request.config.getoption("--os")
    return os

