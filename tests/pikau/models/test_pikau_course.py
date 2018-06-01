from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator

import datetime as dt
from datetime import datetime


class PikauCourseModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()

    def test_pikau_course_str(self):
        pikau_course = self.test_data.create_pikau_course(1)
        self.assertEqual(
            pikau_course.__str__(),
            "Pikau Course 1"
        )

    def test_pikau_course_is_overdue_past_milestone_date(self):
    	pikau_course = self.test_data.create_pikau_course(1)
    	milestone_date = datetime.now() - dt.timedelta(days=30)
    	pikau_course.milestone = self.test_data.create_milestone(1, milestone_date.date())
    	self.assertEqual(
            pikau_course.is_overdue_milestone,
            True
        )

    def test_pikau_course_is_overdue_future_milestone_date(self):
    	pikau_course = self.test_data.create_pikau_course(1)
    	milestone_date = datetime.now() + dt.timedelta(days=30)
    	pikau_course.milestone = self.test_data.create_milestone(1, milestone_date.date())
    	self.assertEqual(
            pikau_course.is_overdue_milestone,
            False
        )

    def test_pikau_course_is_overdue_current_milestone_date(self):
    	pikau_course = self.test_data.create_pikau_course(1)
    	milestone_date = datetime.now()
    	pikau_course.milestone = self.test_data.create_milestone(1, milestone_date.date())
    	self.assertEqual(
            pikau_course.is_overdue_milestone,
            False
        )

    def test_pikau_course_is_overdue_course_complete_past_milestone_date(self):
    	pikau_course = self.test_data.create_pikau_course(1)
    	milestone_date = datetime.now() - dt.timedelta(days=30)
    	pikau_course.milestone = self.test_data.create_milestone(1, milestone_date.date())
    	pikau_course.status = 7
    	self.assertEqual(
            pikau_course.is_overdue_milestone,
            False
        )

    def test_pikau_course_is_overdue_course_complete_future_milestone_date(self):
    	pikau_course = self.test_data.create_pikau_course(1)
    	milestone_date = datetime.now() + dt.timedelta(days=30)
    	pikau_course.milestone = self.test_data.create_milestone(1, milestone_date.date())
    	pikau_course.status = 7
    	self.assertEqual(
            pikau_course.is_overdue_milestone,
            False
        )

    def test_pikau_course_is_overdue_course_complete_current_milestone_date(self):
    	pikau_course = self.test_data.create_pikau_course(1)
    	milestone_date = datetime.now()
    	pikau_course.milestone = self.test_data.create_milestone(1, milestone_date.date())
    	pikau_course.status = 7
    	self.assertEqual(
            pikau_course.is_overdue_milestone,
            False
        )

