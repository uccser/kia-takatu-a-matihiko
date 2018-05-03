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
            progress_outcome = ProgressOutcome(
                slug=progress_outcome_slug,
                name=progress_outcome_data["name"],
                description=progress_outcome_data["description"],
                exemplars=progress_outcome_data["exemplars"],
            )
            progress_outcome.save()

            self.log("Added progress outcome: {}".format(progress_outcome.__str__()))

        self.log("All progress outcomes loaded!\n")
