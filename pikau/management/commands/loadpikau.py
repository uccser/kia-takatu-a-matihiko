"""Module for the custom Django loadpikau command."""

from django.conf import settings
from django.core import management
from pikau.management.commands._GlossaryTermLoader import GlossaryTermLoader
from pikau.management.commands._GoalLoader import GoalLoader
from pikau.management.commands._LevelLoader import LevelLoader
from pikau.management.commands._ProgressOutcomeLoader import ProgressOutcomeLoader
from pikau.management.commands._TagLoader import TagLoader
from pikau.management.commands._TopicLoader import TopicLoader
from pikau.management.commands._PikauCourseLoader import PikauCourseLoader

class Command(management.base.BaseCommand):
    """Required command class for the custom Django loadpikau command."""

    help = "Loads Pīkau into the website"

    def handle(self, *args, **options):
        """Automatically called when the loadpikau command is given."""

        base_path = settings.PIKAU_CONTENT_BASE_PATH
        GlossaryTermLoader(base_path).load()
        GoalLoader(base_path).load()
        LevelLoader(base_path).load()
        ProgressOutcomeLoader(base_path).load()
        TagLoader(base_path).load()
        TopicLoader(base_path).load()
        PikauCourseLoader(base_path).load()
