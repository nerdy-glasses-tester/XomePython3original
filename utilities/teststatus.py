"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custom_logger as cl
import logging
from base.seleniumdriver import SeleniumDriver
from base.appiumdriver import AppiumDriver
from traceback import print_stack

class TestStatus(AppiumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
                    self.log.info("Take screenshot")
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
                self.log.info("Take screenshot")
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenShot(resultMessage)
            self.log.info("Take screenshot")
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName +  " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True