"""Custom loader for loading levels."""

from django.db import transaction
from pikau.models import Level
from utils.BaseLoader import BaseLoader


class LevelLoader(BaseLoader):
    """Custom loader for loading levels."""

    @transaction.atomic
    def load(self):
        """Load the levels into the database."""
        levels = self.load_yaml_file("levels.yaml")

        for level_slug, level_name in levels.items():
            level = Level(
                slug=level_slug,
                name=level_name,
            )
            level.save()

            self.log("Added level: {}".format(level.__str__()))

        self.log("All levels loaded!\n")
