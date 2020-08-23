from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

    log =  cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
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
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getTitle(self, title):
        return self.driver.title

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f'Element found with locator: {locator} and locatorType: {locatorType}')
        except:
            self.log.error(f'Element not found with locator: {locator} and locatorType: {locatorType}')
        return element

    def elementList(self,locator, locatorType="id"):
        # This Get list of elements
        element = None
        try:
            locatorType = locatorType.lower()
            byType= self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info(f'Element list found with locator: {locator} and locatorType: {locatorType}')
        except:
            self.log.error(f'Element list not found with locator: {locator} and locatorType: {locatorType}')
            return element

    def screenShot(self, resultMessage):
        # Take screenshot of the current web page
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenShotDirectory = "../screenshots/"
        relativeFileName = screenShotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenShotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info(f'Screenshot save to directory {destinationFile}')
        except:
            self.log.error("Exception occurs!!!")
            print_stack()

    def elementClick(self, locator="", locatorType="id", element="None"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(f'Clicked on the element with locator: {locator} and locatorType: {locatorType}')
        except:
            self.log.error(f'Cannot click on the element with locator: {locator} and locatorType: {locatorType}')
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f'Sent data on the element with locator: {locator} and locatorType: {locatorType}')
        except:
            self.log.error(f'Cannot send data on the element with locator: {locator} and locatorType: {locatorType}')
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info(f'Element found with locator: {locator} and locatorType: {locatorType}')
                return True
            else:
                self.log.errort(f'Element not found with locator: {locator} and locatorType: {locatorType}')
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
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
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info(f'Element found with locator: {locator} and locatorType: {byType}')
                return True
            else:
                self.log.error(f'Element not found with locator: {locator} and locatorType: {byType}')
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.error("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element

    def scrollBrowser(self, direction="up"):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -800);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 800);")





























# from selenium.webdriver.common.by import By
# # from traceback import print_stack
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
#
#
# class SeleniumDriver():
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def getByType(self, locatorType):
#         locator = locatorType.lower()
#         if locatorType == "id":
#             return By.ID
#         elif locatorType == "name":
#             return By.NAME
#         elif locatorType == "xpath":
#             return By.XPATH
#         elif locatorType == "css":
#             return By.CSS_SELECTOR
#         elif locatorType == "class":
#             return By.CLASS_NAME
#         elif locatorType == "link":
#             return By.LINK_TEXT
#         else:
#             print("Locator type is not supported!!!")
#         return False
#
#
#     def getElement(self, locator, locatorType="id"):
#         element = None
#         try:
#            # locatorVar = locatorType.lower()
#             byType = self.getByType(locatorType)
#             element = self.driver.find_element(byType, locator)
#             print("Element is found")
#         except:
#             print("Element not found")
#             return element
#
#     def elementClick(self, locator, locatorType="id"):
#         try:
#             element = self.getElement(locator, locatorType)
#             element.click()
#             print(f'Clicked on the element with locator: {locator} and locatorType: {locatorType}')
#         except:
#             print(f'Cannot click on the element with locator: {locator} and locatorType: {locatorType}')
#            # print_stack()
#
#     def sendKeys(self, data, locator, locatorType="id"):
#         try:
#             element = self.getElement(locator, locatorType)
#             element.send_keys(data)
#             print(f'Sent data on the element with locator: {locator} and locatorType: {locatorType}')
#         except:
#             print(f'Cannot send data on the element with locator: {locator} and locatorType: {locatorType}')
#            # print_stack()
#
#     def isElementPresent(self, locator, locatorType="id"):
#         try:
#             element = self.getElement(locator, locatorType)
#             if element is not None:
#                 print("Element is found")
#                 return True
#             else:
#                 return False
#         except:
#             print("Element not found")
#             return False
#
#     def elementPresenceCheck(self, locator, byType):
#         try:
#             elementList = self.driver.find_elements(locator, byType)
#             if len(elementList) > 0:
#                 print("Element is found")
#                 return True
#             else:
#                 return False
#         except:
#             print("Element not found")
#             return False
#
#     def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
#         element = None
#         try:
#             byType = self.getByType(locatorType)
#             print("Waiting for maximum :: " + str(timeout) +
#                   " :: seconds for element to be clickable")
#             wait = WebDriverWait(self.driver, 10, poll_frequency=1,
#                                  ignored_exceptions=[NoSuchElementException,
#                                                      ElementNotVisibleException,
#                                                      ElementNotSelectableException])
#             element = wait.until(EC.element_to_be_clickable((byType,
#                                                              "stopFilter_stops-0")))
#             print("Element appeared on the web page")
#         except:
#             print("Element not appeared on the web page")
#            # print_stack()
#         return element
#
#
#
#
#
#
#
#
#
