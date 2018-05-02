"""Module for the custom Django loadpikau command."""

import os.path
from django.core.management.base import BaseCommand
from django.conf import settings
from pikau.management.commands._GlossaryTermsLoader import GlossaryTermsLoader

class Command(BaseCommand):
    """Required command class for the custom Django loadpikau command."""

    help = "Loads Pīkau into the website"

    def handle(self, *args, **options):
        """Automatically called when the loadpikau command is given."""

        base_path = settings.PIKAU_CONTENT_BASE_PATH
        GlossaryTermsLoader(base_path).load()
