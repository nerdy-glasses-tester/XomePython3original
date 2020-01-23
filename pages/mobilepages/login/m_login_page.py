import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
from selenium.common.exceptions import TimeoutException

class MLoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    pkgresrid="com.xome.android:id"
    pkgresridandroid="android:id"
    _permission_at_startup="com.android.packageinstaller:id/permission_allow_button"
    #_permission_at_startup=".//android.widget.Button[contains(text(), 'ALLOW')]"
    _hamburger_icon = "android.widget.ImageButton"
    _sign_in=pkgresrid+"/cont_title" #has text SIGN IN
    _email_field=pkgresrid+"/edittext_login_email"
    _password_field=pkgresrid+"/textview_login_password"
    _login_btn=pkgresrid+"/button_login" #has text Sign In
    _closesigninbox = ".//android.widget.LinearLayout[@resource-id='com.xome.android:id/root_layout']/android.view.ViewGroup/android.widget.ImageButton[@index='0']"
    _searchbox =pkgresrid+"/tvSearch"

    _myxomeheader=".//*[@resource-id='com.xome.android:id/cont_title' and @index='0' and @text='MY XOME']"
    _welcomeusertext = ".//android.widget.TextView[@resource-id='com.xome.android:id/cont_title' and @index='0' and @text='Welcome Automation']"

    _myxomesignout=pkgresrid+"/nav_sign_out" #has text Sign Out
    _signout_popup=pkgresridandroid+"/button1" #has text YES

    _error_msg=pkgresridandroid+"/alertTitle" #has text Error Message
    _emailreq_msg=pkgresridandroid+"/message" #has text email is required
    _error_ok_btn=pkgresridandroid+"/button1" #has text OK

    #_error_msg=pkgresridandroid+"/alertTitle" #has text Error Message #same as above
    _invalidcreds_msg=pkgresridandroid+"/message" #has text Invalid credentials provided
    #_error_ok_btn=pkgresridandroid+"/button1" #has text OK #same as above



    def clickPermissionAtStartup(self):
        try:
            element=self.mobilegetElement(locator=self._permission_at_startup, locatorType="id")
        except:
            self.log.info("Can't find element _permission_at_startup")
        element.click()

    def clickHamburgerMenu(self):
        try:
            element = self.mobilegetElement(locator=self._hamburger_icon, locatorType="class")
        except:
            self.log.info("Can't find element _hamburger_icon")
        element.click()
        self.log.info("Click hamburger menu")

    def clickSignIn(self):
        try:
            element = self.mobilegetElement(locator=self._sign_in, locatorType="id")
        except:
            self.log.info("Can't find element _sign_in")
        element.click()
        time.sleep(3)
        self.log.info("Click sign in")

    def enterEmail(self, email):
        try:
            element= self.mobilegetElement(locator=self._email_field, locatorType="id")
        except:
            self.log.info("Can't find element _email_field")
        element.send_keys(email)
        self.log.info("Enter email")

    def enterPassword(self, password):
        try:
            element = self.mobilegetElement(locator=self._password_field, locatorType="id")
        except:
            self.log.info("Can't find element _password_field")
        element.send_keys(password)
        self.log.info("Enter password")

    def clickLoginButton(self):
        try:
            element = self.mobilegetElement(locator=self._login_btn, locatorType="id")
        except:
            self.log.info("Can't find element _login_btn")
        element.click()
        self.log.info("Click login button")

    def clearFields(self):
        try:
            emailField = self.mobilegetElement(locator=self._email_field, locatorType='id')
        except:
            self.log.info("Can't find element _email_field")
        emailField.clear()
        try:
            passwordField = self.mobilegetElement(locator=self._password_field, locatorType='id')
        except:
            self.log.info("Can't find element _password_field")
        passwordField.clear()
        self.log.info("Clear fields")

    def closeSignInfBox(self):
        try:
            closesigninbox = self.mobilegetElement(locator=self._closesigninbox, locatorType="xpath")
        except:
            self.log.info("Can't find element _closesigninbox")
        closesigninbox.click()
        self.log.info("Closed signin box.")

    def dismissMenuByClickingSearchbox(self):
        try:
            element=self.mobilegetElement(locator=self._searchbox, locatorType="id")
        except:
            self.log.inf("Can't find element _searchbox")
        element.click()
        self.log.info("Dismiss menu by clicking on search box")

    def clickMyXomeHeader(self):
        try:
            myxomeheader = self.mobilegetElement(locator=self._myxomeheader, locatorType="xpath")
        except:
            self.log.info("Can't find element _myxomeheader")
        myxomeheader.click()
        time.sleep(2)
        self.log.info("Open MyXome header")

    def firstlogin(self, email, password, name):
        self.clickHamburgerMenu()
        self.clickSignIn()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(3)
        self.log.info("Completed Login")

    def login(self, email, password, name):
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(3)
        self.log.info("Completed Login")

    def blankLogin(self):
        self.clickHamburgerMenu()
        self.clickSignIn()
        self.clickLoginButton()
        self.log.info("Just completed the blankLogin method")

    def wrongLogin(self, email="", password=""):
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.log.info("Just completed the wrongLogin method")
        time.sleep(3)

    def verifyLoginSuccessful(self, name):
        self.clickHamburgerMenu()
        time.sleep(3)
        element = self.mobilegetElement(locator=self._welcomeusertext, locatorType="xpath")
        self.log.info("Found welcomeusertext element.")
        result = element.text
        self.log.info("Welcome user text is: "+result)
        if result==name:
            self.log.info("***VERIFIED SUCCESSFUL LOGIN.***")
            return True
        else:
            self.log.error("***FAILED TO LOGIN. DID NOT FIND WELCOME USER TEXT.***")
            return False

    def verifyBlankLogin(self):
        error = self.driver.switch_to.alert
        element = error.text
        self.log.info("errormsg is: "+element)
        error.accept()
        time.sleep(2)
        if "email is required" in element:
            self.log.info("TEST PASS: Verified email is required error.")
            return True
        else:
            self.log.error(
                "TEST FAIL: Can't find email is required error message.")
            return False

    def verifyWrongLogin(self):
        error = self.driver.switch_to.alert
        element = error.text
        self.log.info("errormsg is: "+element)
        error.accept()
        time.sleep(3)
        if "Sign In Failed" in element:
            self.log.info("TEST PASS: Verified invalid credentials provided error.")
            return True
        else:
            self.log.error("TEST FAIL: Can't find invalid credentials provided error message.")
            return False

    def logout(self):
        self.clickHamburgerMenu()
        self.clickMyXomeHeader()
        try:
            myxomesignout = self.mobilegetElement(locator=self._myxomesignout, locatorType="id")
        except:
            self.log.info("Can't find element _myxomesignout")
        myxomesignout.click()
        time.sleep(2)
        try:
            signoutpopup = self.mobilegetElement(locator=self._signout_popup, locatorType="id")
        except:
            self.log.info("Can't find element _signout_popup")
        signoutpopup.click()
        time.sleep(3)

    def verifyLogoutSuccessful(self):
        self.clickHamburgerMenu()
        element = self.mobilegetElement(locator=self._sign_in, locatorType="id")
        self.log.info("Found signin element after signed out.")
        if element is not None:
            self.log.info("***SUCCESSFULLY LOGGED OUT.***")
            return True
        else:
            self.log.error("***FAILED TO LOG OUT.***")
            return False
