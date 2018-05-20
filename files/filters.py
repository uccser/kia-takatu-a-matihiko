"""Filters for the files application."""

import django_filters
from files.models import File


class FileFilter(django_filters.FilterSet):
    """File filter for the files table."""

    class Meta:
        """Meta attributes for FileFilter class."""
        model = File
        fields = ["licence"]
