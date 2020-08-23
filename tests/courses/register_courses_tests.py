from pages.courses.register_courses_pages import RegisterCoursePage
from utilities.teststatus import TestStatus
import pytest
import unittest


pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self):
        self.courses = RegisterCoursePage(self)
        self.ts = TestStatus(self)

    pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for Beginners")
        self.courses.enrollCourse(num="", exp="1220", cvv="234")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Test was Failed")


