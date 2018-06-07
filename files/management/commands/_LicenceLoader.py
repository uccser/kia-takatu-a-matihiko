"""Custom loader for loading licences."""

from django.db import transaction
from files.models import Licence
from utils.BaseLoader import BaseLoader


class LicenceLoader(BaseLoader):
    """Custom loader for loading licences."""

    @transaction.atomic
    def load(self):
        """Load the licences into the database."""
        licences = self.load_yaml_file("licences.yaml")

        for licence_slug, licence_data in licences.items():
            defaults = {
                "name": licence_data["name"],
                "url": licence_data["url"],
            }
            licence, created = Licence.objects.update_or_create(
                slug=licence_slug,
                defaults=defaults,
            )
            self.log_object_creation(created, licence)

        self.log("All licences loaded!\n")
