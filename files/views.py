"""Views for the files application."""

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from files.tables import FileTable
from files.filters import FileFilter
from files.models import (
    File,
)


class FileList(LoginRequiredMixin, SingleTableMixin, FilterView):
    """View for the file list page."""

    template_name = "files/index.html"
    model = File
    table_class = FileTable
    filterset_class = FileFilter
