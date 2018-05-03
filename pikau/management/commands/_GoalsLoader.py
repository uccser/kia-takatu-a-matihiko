"""Custom loader for loading goals."""

from django.db import transaction
from pikau.models import Goal
from utils.BaseLoader import BaseLoader


class GoalsLoader(BaseLoader):
    """Custom loader for loading goals."""

    @transaction.atomic
    def load(self):
        """Load the goals into the database."""
        goals = self.load_yaml_file("goals.yaml")

        for goal_slug, goal_description in goals.items():
            goal = Goal(
                slug=goal_slug,
                description=goal_description,
            )
            goal.save()

            self.log("Added goal: {}".format(goal.__str__()))

        self.log("All goals loaded!\n")
