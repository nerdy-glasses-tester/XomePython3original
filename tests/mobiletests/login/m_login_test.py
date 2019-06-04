from base.webdriverFactory import WebDriverFactory
from pages.mobilepages.login.m_login_page import MLoginPage
from utilities.teststatus import TestStatus
import unittest, pytest
import utilities.custom_logger as cl
import logging
import os
from utilities.excel_utils import ExcelUtils as excelutils

@pytest.mark.usefixtures("setUp")
class MLoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    testName = ""

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.wdf = WebDriverFactory(self.browser, self.os)
        self.mlp = MLoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.excel = excelutils(self.driver)

    def get_excel_data(self, testName):
        datafile = os.path.join(self.thisdir, 'testdata/MobileTestData.xlsx')
        self.log.info(datafile)
        data = self.excel.get_input_rows(datafile, testName)
        return data

    @pytest.mark.run(order=1)
    def test_minvalidLoginBlank(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_minvalidLoginBlank++++++++++++++++++++++++++++++++++++")
        self.mlp.clickPermissionAtStartup()
        self.mlp.blankLogin()
        result = self.mlp.verifyBlankLogin()
        self.ts.markFinal("test_minvalidLoginBlank", result, "Verify Can't Login with Blank Fields")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_minvalidLoginBlank++++++++++++++++++++++++++++++++++++")

    @pytest.mark.run(order=2)
    def test_minvalidLoginWrongPassword(self):
        self.log.info(
            "++++++++++++++++++++++++++++++++++++STARTING test_mvalidLoginWrongPassword++++++++++++++++++++++++++++++++++++")
        testName = self._testMethodName
        self.log.info(testName)
        data = self.get_excel_data(testName)
        email = data.get("email")
        password = data.get("password")
        self.mlp.wrongLogin(email, password)
        result = self.mlp.verifyWrongLogin()
        self.ts.markFinal("test_mvalidLoginWrongPassword", result, "Verify Can't Login with Wrong Password")
        self.log.info(
            "++++++++++++++++++++++++++++++++++++ENDING test_mvalidLoginWrongPassword++++++++++++++++++++++++++++++++++++")

    @pytest.mark.run(order=3)
    def test_minvalidLoginWrongEmail(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_minvalidLoginWrongEmail++++++++++++++++++++++++++++++++++++")
        testName = self._testMethodName
        self.log.info(testName)
        data = self.get_excel_data(testName)
        email = data.get("email")
        password = data.get("password")
        self.mlp.wrongLogin(email, password)
        result = self.mlp.verifyWrongLogin()
        self.ts.markFinal("test_minvalidLoginWrongEmail", result, "Verify Can't Login with Wrong Email")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_minvalidLoginWrongEmail++++++++++++++++++++++++++++++++++++")

    @pytest.mark.run(order=4)
    def test_mvalidLogin(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_mvalidLogin++++++++++++++++++++++++++++++++++++")
        testName = self._testMethodName
        self.log.info(testName)
        data = self.get_excel_data(testName)
        email = data.get("email")
        password = data.get("password")
        name = data.get("name")
        self.mlp.login(email, password, name)
        result = self.mlp.verifyLoginSuccessful(name)
        self.mlp.dismissMenuByClickingSearchbox()
        self.ts.markFinal("test_mvalidLogin", result, "Verify Can Login Successfully")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_mvalidLogin++++++++++++++++++++++++++++++++++++")

    @pytest.mark.run(order=5)
    def test_mvalidLogout(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_mvalidLogout++++++++++++++++++++++++++++++++++++")
        self.mlp.logout()
        result = self.mlp.verifyLogoutSuccessful()
        self.ts.markFinal("test_mvalidLogout", result, "Verify Can Logout Successfully")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_mvalidLogout++++++++++++++++++++++++++++++++++++")


#pytest -s -v tests/mobiletests/login/m_login_test.py --browser none --os android --html=htmlreport.html