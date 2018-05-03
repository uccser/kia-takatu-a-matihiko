"""Module for the custom Django loadpikau command."""

from django.conf import settings
from django.core import management
from pikau.management.commands._GlossaryTermsLoader import GlossaryTermsLoader
from pikau.management.commands._GoalsLoader import GoalsLoader
from pikau.management.commands._LevelsLoader import LevelsLoader
from pikau.management.commands._TagsLoader import TagsLoader
from pikau.management.commands._TopicsLoader import TopicsLoader

class Command(management.base.BaseCommand):
    """Required command class for the custom Django loadpikau command."""

    help = "Loads Pīkau into the website"

    def handle(self, *args, **options):
        """Automatically called when the loadpikau command is given."""

        base_path = settings.PIKAU_CONTENT_BASE_PATH
        management.call_command("flush", interactive=False)
        GlossaryTermsLoader(base_path).load()
        GoalsLoader(base_path).load()
        LevelsLoader(base_path).load()
        TagsLoader(base_path).load()
        TopicsLoader(base_path).load()
