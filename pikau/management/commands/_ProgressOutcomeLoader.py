"""Custom loader for loading progress outcomes."""

from django.db import transaction
from pikau.models import ProgressOutcome
from utils.BaseLoader import BaseLoader


class ProgressOutcomeLoader(BaseLoader):
    """Custom loader for loading progress outcomes."""

    @transaction.atomic
    def load(self):
        """Load the progress_outcomes into the database."""
        progress_outcomes = self.load_yaml_file("progress-outcomes.yaml")

        for progress_outcome_slug, progress_outcome_data in progress_outcomes.items():
            defaults = {
                "name": progress_outcome_data["name"],
                "abbreviation": progress_outcome_data["abbreviation"],
                "description": progress_outcome_data["description"],
                "exemplars": progress_outcome_data["exemplars"],
            }
            progress_outcome, created = ProgressOutcome.objects.update_or_create(
                slug=progress_outcome_slug,
                defaults=defaults,
            )
            self.log_object_creation(created, progress_outcome)

        self.log("All progress outcomes loaded!\n")
