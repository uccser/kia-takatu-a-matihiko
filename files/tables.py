"""Tables for the files application."""

import django_tables2 as tables
from files.models import (
    File,
)


class FileTable(tables.Table):
    """Table to display all files."""

    licence = tables.RelatedLinkColumn()

    class Meta:
        """Meta attributes for FileTable class."""

        model = File
        fields = ("filename", "licence")
        order_by = "filename"
