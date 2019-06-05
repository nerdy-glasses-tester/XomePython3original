from base.webdriverFactory import WebDriverFactory
from pages.webpages.login.login_page import LoginPage
from utilities.teststatus import TestStatus
from utilities.excel_utils import ExcelUtils
import unittest, pytest
import utilities.custom_logger as cl
import logging
import os


@pytest.mark.usefixtures("setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    testName = ""

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.wdf = WebDriverFactory(self.browser, self.os)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.excel = ExcelUtils(self.driver)

    def get_excel_data(self, testName):
        datafile = os.path.join('testdata/TestData.xlsx')
        self.log.info(datafile)
        data = self.excel.get_input_rows(datafile, testName)
        return data

    @pytest.mark.run(order=1)
    def test_invalidLoginBlank(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_invalidLoginBlank++++++++++++++++++++++++++++++++++++")
        self.lp.clickSignInLink()
        self.lp.blankLogin()
        result = self.lp.verifyBlankLogin()
        self.ts.markFinal("test_invalidLoginBlank", result, "Verify Can't Login with Blank Fields")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_invalidLoginBlank++++++++++++++++++++++++++++++++++++")

    @pytest.mark.run(order=2)
    def test_invalidLoginWrongPassword(self):
        self.log.info(
            "++++++++++++++++++++++++++++++++++++STARTING test_validLoginWrongPassword++++++++++++++++++++++++++++++++++++")
        testName = self._testMethodName
        self.log.info(testName)
        data = self.get_excel_data(testName)
        email = data.get("email")
        password = data.get("password")
        self.lp.wrongLogin(email, password)
        browser1 = self.wdf.browser
        result = self.lp.verifyWrongLogin(testbrowser=browser1)
        self.ts.markFinal("test_validLoginWrongPassword", result, "Verify Can't Login with Wrong Password")
        self.log.info(
            "++++++++++++++++++++++++++++++++++++ENDING test_validLoginWrongPassword++++++++++++++++++++++++++++++++++++")

    @pytest.mark.run(order=3)
    def test_invalidLoginWrongEmail(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_invalidLoginWrongEmail++++++++++++++++++++++++++++++++++++")
        testName = self._testMethodName
        self.log.info(testName)
        data = self.get_excel_data(testName)
        email = data.get("email")
        password = data.get("password")
        self.lp.wrongLogin(email, password)
        browser1 = self.wdf.browser
        result = self.lp.verifyWrongLogin(testbrowser=browser1)
        self.ts.markFinal("test_invalidLoginWrongEmail", result, "Verify Can't Login with Wrong Email")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_invalidLoginWrongEmail++++++++++++++++++++++++++++++++++++")

    @pytest.mark.run(order=4)
    def test_validLogin(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_validLogin++++++++++++++++++++++++++++++++++++")
        testName = self._testMethodName
        self.log.info(testName)
        data = self.get_excel_data(testName)
        email = data.get("email")
        password = data.get("password")
        name = data.get("name")
        self.lp.login(email, password, name)
        result = self.lp.verifyLoginSuccessful(name)
        self.ts.markFinal("test_validLogin", result, "Verify Can Login Successfully")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_validLogin++++++++++++++++++++++++++++++++++++")

    @pytest.mark.run(order=5)
    def test_validLogout(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_validLogout++++++++++++++++++++++++++++++++++++")
        self.lp.logout()
        result = self.lp.verifyLogoutSuccessful()
        self.ts.markFinal("test_validLogout", result, "Verify Can Logout Successfully")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_validLogout++++++++++++++++++++++++++++++++++++")

#pytest -s -v tests/webtests/login/login_test.py --browser chrome --os none --html=htmlreport.html