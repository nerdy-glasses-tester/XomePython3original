"""
WebDriver Factory class implementation
It creates a webdriver instance based on browser or os configurations

Example:
    wdf = WebDriverFactory(browser, os)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver as webdriver
from appium import webdriver as appdriver
from path import Path
import time
import traceback
import utilities.custom_logger as cl
import logging
import os

class WebDriverFactory():

    log = cl.customLogger(logging.DEBUG)

    #thisdir = os.path.dirname(os.path.abspath(__file__))
    thisdir = "/Users/angee/PycharmProjects/XomePython3/"

    def __init__(self, browser, os):
        self.browser = browser
        self.os = os

    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
        # Setting browser drivers path for selenium
        export PATH="/Users/angee/seleniumgrid:${PATH}"
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://www.xome.com/"

        items = []

        if self.browser != "none" and self.os == "none":
            if self.browser == "safari":
                driver = webdriver.Safari()
                self.log.info("Running Safari Tests")
            elif self.browser == "firefox":
                #driver = webdriver.Firefox(executable_path=r'./zfiles/geckodriver')
                driverpath = os.path.join(self.thisdir, 'zfiles/geckodriver')
                driver = webdriver.Firefox(executable_path=driverpath)
                self.log.info("Running Firefox Tests")
            elif self.browser == "chrome":
                # Set chrome driver
                #driver = webdriver.Chrome(executable_path=r'./zfiles/chromedriver')
                driverpath = os.path.join(self.thisdir, 'zfiles/chromedriver')
                driver = webdriver.Chrome(executable_path=driverpath)
                self.log.info("Running Chrome Tests")

            # Loading browser with App URL
            driver.get(baseURL)

            # Maximize the window
            driver.maximize_window()
            driver.set_window_size(1440, 900)  # mac 15inch screen resolution
            time.sleep(5)

            # Setting Driver Implicit Time out for An Element
            driver.implicitly_wait(30)

            items.append(driver)
            items.append(self.browser)
            items.append(self.os)
            items.append(self.thisdir)
            return items


        elif self.browser == "none" and self.os != "none":
            desired_caps = {}
            if self.os == "android":
                desired_caps['platformName'] = 'Android'
                desired_caps['platformVersion'] = '7.1.1'
                desired_caps['automationName'] = 'uiautomator2'
                desired_caps['deviceName'] = 'Nexus'
                desired_caps['appPackage'] = "com.xome.android"
                #adb shell dumpsys window windows|grep -E 'mCurrentFocus' to get app info
                desired_caps['appActivity'] = "com.xome.android.ui.map.MapActivity2"
                #desired_caps['appActivity'] = "com.xome.android.feature.mapsearch.view.MapActivity2"
                desired_caps['newCommandTimeout'] = 120
                #desired_caps['app'] = Path('../zfiles/base.apk')
                appzpath = os.path.join(self.thisdir, 'zfiles/base.apk')
                desired_caps['app'] = Path(appzpath)

                driver = appdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
                self.log.info("Running Android Tests")

                items.append(driver)
                items.append(self.browser)
                items.append(self.os)
                items.append(self.thisdir)
                return items

            elif self.os == "ios":
                desired_caps['platformName'] = 'iOS'
                desired_caps['platformVersion'] = '10.3.3'
                desired_caps['automationName'] = 'xcuitest'
                desired_caps['deviceName'] = 'iPhone 5'
                desired_caps['udid'] = '8319807bbbc1d04c9bbc0634e14d28aca946b536'
                desired_caps['xcodeOrgid'] = 'Angela Tong'
                desired_caps['xcodeSigningId'] = 'iPhone Developer'
                desired_caps['newCommandTimeout'] = 120
                #desired_caps['app'] = Path('../zfiles/base.apk')
                appzpath = os.path.join(self.thisdir, 'zfiles/base.ipa')
                desired_caps['app'] = Path(appzpath)
                driver = appdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
                self.log.info("Running iOS Tests")


                items.append(driver)
                items.append(self.browser)
                items.append(self.os)
                items.append(self.thisdir)
                return items

        else:
            self.log.info("Have to enter a value for both browser and os. Please enter --browser none for appium automation or --os none for selenium automation")



