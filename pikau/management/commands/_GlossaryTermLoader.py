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
            term_definition = term_data["definition"]
            defaults = {
                "term": term_name,
                "definition": term_definition,
            }
            glossary_term, created = GlossaryTerm.objects.update_or_create(
                slug=term_slug,
                defaults=defaults,
            )
            self.log_object_creation(created, glossary_term)

        self.log("All glossary terms loaded!\n")
