from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.home.navigation_page import NavigationPage


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.np = NavigationPage(self.driver)

    # Locators
    loginLink = "Login"
    emailField = "user_email"
    passwordField = "user_password"
    loginButton = "commit"

    def clickLoginLink(self):
        self.elementClick(self.loginLink, locatorType="link")

    def clearFields(self):
        emailField = self.getElement(self.emailField)
        emailField.clear()
        passwordField = self.getElement(self.passwordField)
        passwordField.clear()

    def enterEmail(self, email):
        self.sendKeys(email, self.emailField)

    def enterPassword(self, password):
        self.sendKeys(password, self.passwordField)

    def clickLoginButton(self):
        self.elementClick(self.loginButton, locatorType="name")

    def login(self, email, password):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    # method to verify successful login
    def verifyLoginSuccessful(self):
        result = self.isElementPresent("search-courses", locatorType="id")
        return result

    def verifyLoginNotSuccessful(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]", locatorType="xpath")
        return result

    # def verifyTitle(self):
    #     if "Let's Kode it" in self.getTitle():
    #         return True
    #     else:
    #         return False

    def verifyTitle(self):
        return self.getTitle("Let's Kode it")

    def logOut(self):
        self.np.navigateToUserIcon()
        self.elementClick(locator="//div[@id='navbar']//a[@href='/Log Out']", locatorType="xpath")


























# from base.selenium_driver import SeleniumDriver
#
# class LoginPage(SeleniumDriver):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#
#     # locators
#     loginLink = "Login"
#     emailField = "user_email"
#     passwordField = "user_password"
#     loginButton = "commit"  # name
#
#     # Action perform on each element
#     def clickLoginLink(self):
#         self.elementClick(self.loginLink, locatorType="link")
#
#     def enterEmail(self, email):
#         self.sendKeys(email, self.emailField)
#
#     def enterPassword(self, password):
#         self.sendKeys(password, self.passwordField)
#
#     def clickLoginButton(self):
#         self.elementClick(self.loginButton, locatorType="name")
#
#     # This wrap all the functionality within one method
#     def login(self, email, password):
#         self.clickLoginLink()
#         self.enterEmail(email)
#         self.enterPassword(password)
#         self.clickLoginButton()
#
#
#
#
