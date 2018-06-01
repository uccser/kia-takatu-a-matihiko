from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator

from pikau.models import Milestone

from django.db import IntegrityError
from django.template import defaultfilters

import datetime as dt
from datetime import datetime


class MilestoneModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()
        self.current_time = datetime.now()

    def test_milestone_model_one_milestone(self):
        milestone = self.test_data.create_milestone(1, self.current_time)
        query_result = Milestone.objects.get(name="milestone-1")
        self.assertEqual(query_result, milestone)

    def test_milestone_model_two_milestones(self):
        date_1 = self.current_time
        date_2 = self.current_time + dt.timedelta(days=30)
        milestone_1 = self.test_data.create_milestone(1, date_1)
        milestone_2 = self.test_data.create_milestone(2, date_2)
        self.assertQuerysetEqual(
            Milestone.objects.all(),
            [
                "<Milestone: milestone-1 - {}>".format(defaultfilters.date(date_1)),
                "<Milestone: milestone-2 - {}>".format(defaultfilters.date(date_2)),
            ],
            ordered=False
        )

    def test_milestone_model_uniqueness(self):
        date = self.current_time
        milestone = self.test_data.create_milestone(1, date)
        self.assertRaises(
            IntegrityError, 
            lambda: self.test_data.create_milestone(1, date), 
        )

    def test_milestone_model_str(self):
        date = self.current_time
        milestone = self.test_data.create_milestone(1, date)
        self.assertEqual(
            milestone.__str__(),
            "milestone-1 - {}".format(defaultfilters.date(date))
        )

    def test_milestone_model_is_upcoming_future_date(self):
        future_date = self.current_time + dt.timedelta(days=30)
        milestone = self.test_data.create_milestone(1, future_date.date())
        self.assertIs(milestone.is_upcoming, True)

    def test_milestone_model_is_upcoming_past_date(self):
        past_date = self.current_time - dt.timedelta(days=30)
        milestone = self.test_data.create_milestone(1, past_date.date())
        self.assertIs(milestone.is_upcoming, False)

    def test_milestone_model_ordering(self):
        date_1 = self.current_time
        date_2 = self.current_time + dt.timedelta(days=30)
        milestone_1 = self.test_data.create_milestone(1, date_2)
        milestone_2 = self.test_data.create_milestone(2, date_1)
        self.assertQuerysetEqual(
            Milestone.objects.all(),
            [
                "<Milestone: milestone-2 - {}>".format(defaultfilters.date(date_1)),
                "<Milestone: milestone-1 - {}>".format(defaultfilters.date(date_2)),
            ],
        )
