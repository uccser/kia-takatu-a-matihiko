"""Module for the custom Django loadlicences command."""

from django.conf import settings
from django.core import management
from files.management.commands._LicenceLoader import LicenceLoader


class Command(management.base.BaseCommand):
    """Required command class for the custom Django loadlicences command."""

    help = "Loads licences into the website"

    def handle(self, *args, **options):
        """Automatically called when the loadlicences command is given."""
        base_path = settings.FILES_CONTENT_BASE_PATH
        LicenceLoader(base_path).load()
