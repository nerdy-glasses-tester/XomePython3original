"""
Base Page Class Implementation
It implements methods which are common to all the pages.
This class needs to be inherited by all the page classes.
This should not be used by creating object instances.

EX: Class LoginPage(BasePage)

This is an expanded/modified version of the framework sample used in the Selenium Python3 course I enrolled in at https://www.letskodeit.com/
I'm applying it to the XOME web and mobile app instead of the letskodeit web app.
I expanded the teacher's existing framework to include for Appium mobile automation which the course did not cover.
Thanks.
Angela Tong

"""
from base.seleniumdriver import SeleniumDriver
from base.appiumdriver import AppiumDriver

class BasePage(AppiumDriver):

    def __init__(self, driver):
        # super(BasePage, self).__init__(driver) this is python 2 same as super().__init__(driver)
        super().__init__(driver)
        self.driver = driver


        #webview
        #handlelist = self.driver.contexts;
        #for handle in handlelist:
        #    self.log.info(handle)
        #self.driver.context("WEBVIEW_com.example.testapp");