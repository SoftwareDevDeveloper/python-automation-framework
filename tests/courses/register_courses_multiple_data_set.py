from pages.courses.register_courses_pages import RegisterCoursePage
from utilities.teststatus import TestStatus
import pytest
import unittest
from ddt import ddt, data, unpack


# Data Driven test implementation

pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self):
        self.course = RegisterCoursePage(self)
        self.ts = TestStatus(self)

    pytest.mark.run(order=1)
    @data(("JavaScript for Beginners", "10", "1220", "10"), ("Selenium WebDriver with Java ", "12", "0923", "16"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.course.enterCourseName(courseName)
        self.course.selectCourseToEnroll(courseName)
        self.course.enrollCourse(num="ccNum", exp="ccExp", cvv="ccCVV")
        result = self.course.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Test Enrollment Failed")

        self.driver.find_element_by_link_text("All Courses").click()
        self.driver.get("")


