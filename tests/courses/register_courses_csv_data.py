from pages.courses.register_courses_pages import RegisterCoursePage
from utilities.teststatus import TestStatus
import pytest
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time
from pages.home.navigation_page import NavigationPage


# Data Driven test implementation
# Reading text from a csv file

pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self):
        self.course = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.np = NavigationPage(self.driver)

    def setUp(self):
        self.np.navigateToAllCourses()
        # self.driver.find_element_by_link_text("All Courses").click()

    pytest.mark.run(order=1)
    # @data(("JavaScript for Beginners", "10", "1220", "10"), ("Selenium WebDriver with Java ", "12", "0923", "16"))
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.course.enterCourseName(courseName)
        time.sleep(1)
        self.course.selectCourseToEnroll(courseName)
        time.sleep(2)
        self.course.enrollCourse(num="ccNum", exp="ccExp", cvv="ccCVV")
        time.sleep(1)
        result = self.course.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Test Enrollment Failed")

