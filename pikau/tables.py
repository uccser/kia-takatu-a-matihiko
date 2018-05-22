"""Tables for the pikau application."""

import django_tables2 as tables
from pikau.models import (
    GlossaryTerm,
)


class GlossaryTermTable(tables.Table):
    """Table to display all glossary terms."""

    term = tables.LinkColumn()
    slug = tables.TemplateColumn(template_code="<code>{{ record.slug }}</code>")

    class Meta:
        """Meta attributes for GlossaryTermTable class."""

        model = GlossaryTerm
        fields = ("term", "slug", "description")
        order_by = "term"
        attrs = {"class": "table table-hover"}
