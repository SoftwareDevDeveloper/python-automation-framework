from utilities import custom_logger as cl
from base.selenium_driver import SeleniumDriver
import logging


class NavigationPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    myCourses = "My Courses"
    AllCourses = "All Courses"
    practice = "Practice"
    userIconSettings = "//div[@id='navbar']//li[@class='dropdown']"

    def navigateToMyCourses(self):
        self.elementClick(locator=self.myCourses, locatorType="link")

    def navigateToAllCourses(self):
        self.elementClick(locator=self.AllCourses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self.practice, locatorType="link")

    def navigateToUserIcon(self):
        self.elementClick(locator=self.userIconSettings, locatorType="xpath")





