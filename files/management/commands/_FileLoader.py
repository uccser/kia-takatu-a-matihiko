"""Custom loader for loading files."""

from django.db import transaction
from files.models import File, Licence
from utils.BaseLoader import BaseLoader


class FileLoader(BaseLoader):
    """Custom loader for loading files."""

    @transaction.atomic
    def load(self):
        """Load the files into the database."""
        files = self.load_yaml_file("files.yaml")

        for file_slug, file_data in files.items():
            licence = Licence.objects.get(slug=file_data.get("licence", "unknown"))
            defaults = {
                "name": file_data["name"],
                "filename": file_data["filename"],
                "location": file_data["location"],
                "direct_link": file_data.get("direct-link", ""),
                "licence": licence,
                "description": file_data.get("description", ""),
            }
            file_object, created = File.objects.update_or_create(
                slug=file_slug,
                defaults=defaults,
            )
            self.log_object_creation(created, file_object)

        self.log("All files loaded!\n")
