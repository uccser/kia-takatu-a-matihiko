"""Custom loader for loading goals."""

from django.db import transaction
from pikau.models import Tag
from utils.BaseLoader import BaseLoader


class TagLoader(BaseLoader):
    """Custom loader for loading tags."""

    @transaction.atomic
    def load(self):
        """Load the tags into the database."""
        tags = self.load_yaml_file("tags.yaml")

        for tag_slug, tag_data in tags.items():
            defaults = {
                "name": tag_data["name"],
                "description": tag_data.get("description", ""),
            }
            tag, created = Tag.objects.update_or_create(
                slug=tag_slug,
                defaults=defaults,
            )
            self.log_object_creation(created, tag)

        self.log("All tags loaded!\n")
