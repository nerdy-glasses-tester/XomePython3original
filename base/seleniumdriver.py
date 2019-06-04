from selenium.webdriver import ActionChains
from datetime import datetime
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

        log = cl.customLogger(logging.DEBUG)

        def __init__(self, driver):
            self.driver = driver

        def screenShot(self, resultMessage):
            """
            Takes screenshot of the current open page
            """
            dateTimeObj = datetime.now()
            dateObj = dateTimeObj.date()
            timeObj = dateTimeObj.time()
            dateStr = dateObj.strftime("%b%d%Y")
            timeStr = timeObj.strftime("%H.%M.%S.%f")
            fileName = resultMessage + "." + dateStr + timeStr + ".png"
            screenshotDirectory = "../zscreenshots/"
            relativeFileName = screenshotDirectory + fileName
            currentDirectory = os.path.dirname(__file__)
            destinationFile = os.path.join(currentDirectory, relativeFileName)
            destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
            self.log.info("destinationDirectory is: "+destinationDirectory)

            try:
                if not os.path.exists(destinationDirectory):
                    os.makedirs(destinationDirectory)
                self.driver.save_screenshot(destinationFile)
                self.log.info("Screenshot save to directory: " + destinationFile)
            except:
                self.log.error("### Exception Occurred when taking screenshot")
                print_stack()

        def getTitle(self):
            return self.driver.title

        def getByType(self, locatorType):
            locatorType = locatorType.lower()
            if locatorType == "id":
                return By.ID
            elif locatorType == "accessibility_id":
                return By.ACCESSIBILITY_ID
            elif locatorType == "name":
                return By.NAME
            elif locatorType == "xpath":
                return By.XPATH
            elif locatorType == "css":
                return By.CSS_SELECTOR
            elif locatorType == "class":
                return By.CLASS_NAME
            elif locatorType == "link":
                return By.LINK_TEXT
            elif locatorType == "tag":
                return By.TAG_NAME
            else:
                self.log.info("Locator type " + locatorType +
                              " not correct/supported")
            return False

        def getElement(self, locator, locatorType="id"):
            element = None
            try:
                #this is already in waitForElement so comment out
                #locatorType = locatorType.lower()
                #byType = self.getByType(locatorType)
                element = self.waitForElement(locator, locatorType, timeout=30, pollFrequency=0.5)
                if element != None:
                    self.log.info("Element found with locator: " + locator +
                              " and  locatorType: " + locatorType)
                else:
                    self.log.info("Element not found with locator: " + locator + " and locatorType: "+ locatorType)
            except:
                self.log.info("Element not found with locator: " + locator +
                              " and  locatorType: " + locatorType)
            return element

        def getElementList(self, locator, locatorType="id"):
            """
            Get list of elements
            """
            elementList = []
            try:
                locatorType = locatorType.lower()
                byType = self.getByType(locatorType)
                elementList = elementList.append(self.waitForElements(byType, locator, timeout=30, pollFrequency=0.5))
                self.log.info("Element list found with locator: " + locator +
                              " and  locatorType: " + locatorType)
            except:
                self.log.info("Element list not found with locator: " + locator +
                              " and  locatorType: " + locatorType)
            return elementList

        def isElementPresent(self, locator, locatorType="id", element=None):
            """
            Check if element is present -> MODIFIED
            Either provide element or a combination of locator and locatorType
            """
            try:
                if locator:  # This means if locator is not empty
                    element = self.getElement(locator, locatorType)
                if element is not None:
                    self.log.info("Element present with locator: " + locator +
                                  " locatorType: " + locatorType)
                    return True
                else:
                    self.log.info("Element not present with locator: " + locator +
                                  " locatorType: " + locatorType)
                    return False
            except:
                print("Element not found")
                return False

        def isElementDisplayed(self, locator, locatorType="id", element=None):
            """
            NEW METHOD
            Check if element is displayed
            Either provide element or a combination of locator and locatorType
            """
            isDisplayed = False
            try:
                if locator:  # This means if locator is not empty
                    element = self.getElement(locator, locatorType)
                if element is not None:
                    isDisplayed = element.is_displayed()
                    self.log.info("Element is displayed with locator: " + locator +
                                  " locatorType: " + locatorType)
                else:
                    self.log.info("Element not displayed with locator: " + locator +
                                  " locatorType: " + locatorType)
                return isDisplayed
            except:
                print("Element not found")
                return False

        def elementPresenceCheck(self, locator, byType):
            """
            Check if element is present
            """
            try:
                elementList = self.getElementList(byType, locator)
                if len(elementList) > 0:
                    self.log.info("Element present with locator: " + locator +
                                  " locatorType: " + str(byType))
                    return True
                else:
                    self.log.info("Element not present with locator: " + locator +
                                  " locatorType: " + str(byType))
                    return False
            except:
                self.log.info("Element not found")
                return False


        def waitForElement(self, locator, locatorType="id",
                           timeout=30, pollFrequency=0.5):
            element = None
            try:
                byType = self.getByType(locatorType)
                self.log.info("Waiting for maximum :: " + str(timeout) +
                              " :: seconds for element to be clickable")
                wait = WebDriverWait(self.driver, timeout=timeout,
                                     poll_frequency=pollFrequency,
                                     ignored_exceptions=[NoSuchElementException,
                                                         ElementNotVisibleException,
                                                         ElementNotSelectableException])
                element = wait.until(EC.element_to_be_clickable((byType, locator)))
                self.log.info("Wait for element and found.")
            except:
                self.log.info("Wait for element but was not found.")
                print_stack()
            return element

        def waitForElements(self, locator, locatorType="id",
                           timeout=30, pollFrequency=0.5):
            elementList = []
            try:
                byType = self.getByType(locatorType)
                self.log.info("Waiting for maximum :: " + str(timeout) +
                              " :: seconds for element to be clickable")
                wait = WebDriverWait(self.driver, timeout=timeout,
                                     poll_frequency=pollFrequency,
                                     ignored_exceptions=[NoSuchElementException,
                                                         ElementNotVisibleException,
                                                         ElementNotSelectableException])
                elementList = elementList.append(wait.until(EC.presence_of_all_elements_located((byType, locator))))
                self.log.info("Elements appeared on the page")
            except:
                self.log.info("Element(s) did not appeared on the page")
                print_stack()
            return elementList

        def webScroll(self, direction="up"):
            if direction == "up":
                # Scroll Up
                self.driver.execute_script("window.scrollBy(0, -1000);")
                self.log.info("Scroll up")

            if direction == "down":
                # Scroll Down
                self.driver.execute_script("window.scrollBy(0, 1000);")
                self.log.info("Scroll down")

            if direction == "upalittle":
                # Scroll Up
                self.driver.execute_script("window.scrollBy(0, -400);")
                self.log.info("Scroll up a little")

            if direction == "downalittle":
                # Scroll Down
                self.driver.execute_script("window.scrollBy(0, 400);")
                self.log.info("Scroll down a little")

        def switchtoframe(self, locator="", locatorType="name"):
            try:
                element = self.getElement(locator, locatorType)
                self.driver.switch_to.frame(element)
                self.log.info("Switched to iframe found by locator "+locator)
            except:
                self.log.info("Can not switch to iframe: " + locator + " locatorType: " + locatorType)


        def switchtodefaultcontent(self):
            self.driver.switch_to.default_content()
            self.log.info("Switch back to default content")

        def selectDropDown(self, locator="", locatorType="css", value=""):
            dropdown = Select(self.getElement(locator, locatorType))
            dropdown.select_by_visible_text(value)
            self.log.info("Select dropdown value "+value)

        def mouseOver(self, element):
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info("Mouse over to element")

