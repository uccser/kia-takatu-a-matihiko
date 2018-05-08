"""Custom loader for loading topics."""

from django.db import transaction
from pikau.models import Topic
from utils.BaseLoader import BaseLoader


class TopicLoader(BaseLoader):
    """Custom loader for loading topics."""

    @transaction.atomic
    def load(self):
        """Load the topics into the database."""
        topics = self.load_yaml_file("topics.yaml")

        for topic_slug, topic_name in topics.items():
            defaults = {
                "name": topic_name,
            }
            topic, created = Topic.objects.update_or_create(
                slug=topic_slug,
                defaults=defaults,
            )
            self.log_object_creation(created, topic)

        self.log("All topics loaded!\n")
