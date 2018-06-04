from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator

from pikau.models import Goal
from django.db import IntegrityError


class GoalModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()

    def test_goal_model_one_goal(self):
        goal = self.test_data.create_goal(1)
        query_result = Goal.objects.get(slug="goal-1")
        self.assertEqual(query_result, goal)

    def test_goal_model_two_goals(self):
        self.test_data.create_goal(1)
        self.test_data.create_goal(2)
        self.assertQuerysetEqual(
            Goal.objects.all(),
            [
                "<Goal: <p>Description for goal 1.</p>>",
                "<Goal: <p>Description for goal 2.</p>>"
            ],
            ordered=False
        )

    def test_goal_model_uniqueness(self):
        self.test_data.create_goal(1)
        self.assertRaises(
            IntegrityError,
            lambda: self.test_data.create_goal(1)
        )

    def test_goal_model_str(self):
        goal = self.test_data.create_goal(1)
        self.assertEqual(
            goal.__str__(),
            "<p>Description for goal 1.</p>"
        )
