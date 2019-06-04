import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _signin_link = "div.user-section>a.LinkButton.btn.btn-secondary"
    _login_iframe = "login-iframe"
    _email_field = "security_loginname"
    _password_field = "security_password"
    _login_btn = "submit-button"
    _loggedin_username = ".//div[@class='NavSubmenu btn-group ']/div[@id='uniqid-NavSubmenu-button-14']/span[@class='NavItem top-level user-menu']/span"
    _signout_link = ".//a[@class='NavItem user-nav-item link' and contains(text(), 'Sign Out')]"
    _wrong_pwd_email_error = ".//div[@class='row-fluid errorMessageBox errorMessageBoxServerSide']/ul/li"
    _sign_in_header = ".//h2[contains(text(), 'Sign In')]"

    def clickSignInLink(self):
        element = self.getElement(locator=self._signin_link, locatorType="css")
        element.click()
        self.switchtoframe(locator=self._login_iframe, locatorType="class")
        self.log.info("Click SignIn Link")

    def enterEmail(self, email):
        element = self.getElement(locator=self._email_field, locatorType='id')
        element.click()
        element.send_keys(email)
        self.log.info("Enter Email")

    def enterPassword(self, password):
        element = self.getElement(locator=self._password_field, locatorType='id')
        element.click()
        element.send_keys(password)
        self.log.info("Enter Password")

    def clickLoginButton(self):
        element = self.getElement(locator=self._login_btn, locatorType="id")
        element.click()
        self.log.info("Click Login Button")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field, locatorType='id')
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field, locatorType='id')
        passwordField.clear()
        self.log.info("Clear fields")

    def firstlogin(self, email="", password="", name=""):
        self.clickSignInLink()
        self.switchtoframe(locator=self._login_iframe, locatorType="class")
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.log.info("Just completed the first login")

    def login(self, email="", password="", name=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.log.info("Just completed the login method")
        time.sleep(3)

    def blankLogin(self):
        self.clickLoginButton()
        self.log.info("Just completed the blankLogin method")

    def wrongLogin(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.log.info("Just completed the wrongLogin method")

    def verifyWrongLogin(self, testbrowser=""):
        self.log.info("browser: "+testbrowser)
        if testbrowser =="safari":
            time.sleep(1)
        element = self.getElement(locator=self._wrong_pwd_email_error, locatorType="xpath")
        error = element.get_attribute("innerText")
        self.log.info("Error text found on page is: "+error)
        if error == "Oops, the e-mail or password doesn't match.":
            self.log.info("TEST PASS: Verified error for wrong login. Oops, the e-mail or password doesn't match.")
            return True
        else:
            self.log.error("TEST FAIL: Failed to verify the error for wrong login - Oops, the e-mail or password doesn't match.")
            return False

    def verifyBlankLogin(self):
        signin_header = self.getElement(locator=self._sign_in_header, locatorType="xpath")
        if signin_header is not None:
            self.log.info("TEST PASS: Verified signin header is still present for blank login.")
            return True
        else:
            self.log.error("TEST FAIL: Did not find signin header. Can't confirm blank login did not allow you to login and still stay on signin screen.")
            return False

    def verifyLoginSuccessful(self, name=""):
        self.switchtodefaultcontent()
        element = self.getElement(locator=self._loggedin_username, locatorType="xpath")
        if element is not None:
            self.log.info("Element was found. Now getting its text.")
            username = element.text
            self.log.info("Username is "+username)
            self.log.info("***VERIFIED SUCCESSFUL LOGIN.***")
            return username.upper() == name
        else:
            self.log.error("***FAILED TO LOGIN. DID NOT FIND LOGGED IN USER.***")
            return False

    def logout(self):
        loginusername_element = self.getElement(locator=self._loggedin_username, locatorType="xpath")
        self.mouseOver(loginusername_element)
        signout_element = self.getElement(locator=self._signout_link, locatorType="xpath")
        signout_element.click()
        self.log.info("Just completed the logout method")
        time.sleep(3)

    def verifyLogoutSuccessful(self):
        element = self.getElement(locator=self._signin_link, locatorType="css")
        if element is not None:
            self.log.info("***SUCCESSFULLY LOGGED OUT.***")
            return True
        else:
            self.log.error("***FAILED TO LOG OUT.***")
            return False