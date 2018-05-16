"""Custom loader for loading goals."""

from django.db import transaction
from pikau.models import Goal
from utils.BaseLoader import BaseLoader


class GoalLoader(BaseLoader):
    """Custom loader for loading goals."""

    @transaction.atomic
    def load(self):
        """Load the goals into the database."""
        goals = self.load_yaml_file("goals.yaml")

        for goal_slug, goal_description in goals.items():
            defaults = {
                "description": goal_description,
            }
            goal, created = Goal.objects.update_or_create(
                slug=goal_slug,
                defaults=defaults,
            )
            self.log_object_creation(created, goal)

        self.log("All goals loaded!\n")
