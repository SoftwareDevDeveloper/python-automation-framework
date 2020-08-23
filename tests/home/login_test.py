from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

class LoginTests(unittest.TestCase):
    driver = webdriver.Firefox()
    baseURL = "https://letskodeit.teachable.com/"
    driver.maximize_window()
    driver.implicitly_wait(23)
    lp = LoginPage(driver)
    ts = TestStatus(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("ruufman@gmail.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title is Incorrect")
        # assert result1 == True
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login not successful")
        # assert result2 == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logOut()
        self.driver.get(self.baseURL)
        self.lp.login("ruufman@gmail.com", "abcabcloginabcabc")
        result = self.lp.verifyLoginNotSuccessful()
        assert result == True















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from pages.home.login_page import LoginPage
# import unittest
#
#
# class LoginTests(unittest.TestCase):
#
#     def test_validLogin(self):
#         baseURL = "https://letskodeit.teachable.com/"
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         driver.implicitly_wait(3)
#         driver.get(baseURL)
#
#         lp = LoginPage(driver)
#         lp.login("ruufman@gmail.com", "abcabc")
#
#         loginSuccess = driver.find_element(By.ID, "query")
#         if loginSuccess is not None:
#             print("Login was Successful")
#         else:
#             print("Login failed")
#
#
#
#
#
#
