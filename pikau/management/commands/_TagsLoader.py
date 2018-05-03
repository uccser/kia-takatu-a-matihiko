"""Custom loader for loading goals."""

from django.db import transaction
from pikau.models import Tag
from utils.BaseLoader import BaseLoader


class TagsLoader(BaseLoader):
    """Custom loader for loading tags."""

    @transaction.atomic
    def load(self):
        """Load the tags into the database."""
        tags = self.load_yaml_file("tags.yaml")

        for tag_slug, tag_name in tags.items():
            tag = Tag(
                slug=tag_slug,
                name=tag_name,
            )
            tag.save()

            self.log("Added tag: {}".format(tag.__str__()))

        self.log("All tags loaded!\n")
