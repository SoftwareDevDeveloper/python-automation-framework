from utilities import custom_logger as cl
from base.selenium_driver import SeleniumDriver
import logging


class RegisterCoursePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    searchBox = "search-courses"  # id
    course = "//div[contains(@class, 'course-listing-title') and contains(text(),'{0}')]"
    enrollButton = "enroll-button-top"  # id
    ccNum = "cardnumber"  # name
    expDate = "exp-date"  # name
    cvvNum = "cvc"        # name
    submitButton = "//div[@id='react-checkout']/div/div/div[@role='none']//div[@id='new_card']//button[contains(text(),'Buy Now $118.80')]"
    enrollErrorMessage = "//div[@id='credit-card']/div[@class='N-9Xr _1_C4M']/div[@class='p-3-xs']/div/div/div/div[@class='dsp-flex-xs flex-direction-column m-b-3-xs']//span[@role='alert']"
    agreeTermsCheckBox = "saveCard"   # id

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self.searchBox)

    def selectCourseToEnroll(self, fullCourseNAme):
        self.elementClick(locator=self.course.format(fullCourseNAme), locatorType="xpath")

    def clickEnrollButton(self):
        self.elementClick(locator=self.enrollButton)

    def enterCardNumber(self, num):
        self.sendKeys(num, locator=self.ccNum, locatorType="name")

    def enterCardExp(self, exp):
        self.sendKeys(exp, locator=self.expDate, locatorType="name")

    def enterCardCVC(self, cvv):
        self.sendKeys(cvv, locator=self.cvvNum, locatorType="name")

    def clickAgreeToTermsCheckBox(self):
        self.elementClick(locator=self.agreeTermsCheckBox)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self.submitButton, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNumber(num)
        self.enterCardExp(exp)
        self.enterCardCVC(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickEnrollButton()
        self.scrollBrowser(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickAgreeToTermsCheckBox()
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self.enrollErrorMessage, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result








