"""Views for the files application."""

from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin
from files.tables import FileTable
from files.models import (
    File,
)


class FileList(LoginRequiredMixin, SingleTableView):
    """View for the file list page."""

    template_name = "files/index.html"
    model = File
    table_class = FileTable
