"""Views for the files application."""

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from files.models import (
    File,
)


class FileList(LoginRequiredMixin, generic.ListView):
    """View for the file list page."""

    template_name = "files/index.html"
    context_object_name = "files"
    model = File
