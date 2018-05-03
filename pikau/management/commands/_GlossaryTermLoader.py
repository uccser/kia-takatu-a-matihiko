"""Custom loader for loading glossary terms."""

from django.db import transaction
from pikau.models import GlossaryTerm
from utils.BaseLoader import BaseLoader


class GlossaryTermLoader(BaseLoader):
    """Custom loader for loading glossary terms."""

    @transaction.atomic
    def load(self):
        """Load the glossary content into the database."""
        glossary_data = self.load_yaml_file("glossary.yaml")

        for term_slug, term_data in glossary_data.items():
            term_name = term_data["term"]
            term_description = term_data["description"]
            glossary_term = GlossaryTerm(
                slug=term_slug,
                term=term_name,
                description=term_description,
            )
            glossary_term.save()

            self.log("Added glossary term: {}".format(glossary_term.__str__()))

        self.log("All glossary terms loaded!\n")
