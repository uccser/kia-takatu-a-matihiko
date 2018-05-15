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
            defaults = {
                "name": level_name,
            }
            level, created = Level.objects.update_or_create(
                slug=level_slug,
                defaults=defaults,
            )
            self.log_object_creation(created, level)

        self.log("All levels loaded!\n")
