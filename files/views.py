"""Views for the files application."""

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
)
from files.tables import FileTable
from files.filters import FileFilter
from files.models import (
    File,
)
from files.forms import (
    FileForm,
)


class FileList(LoginRequiredMixin, SingleTableMixin, FilterView):
    """View for the file list page."""

    template_name = "files/file_list.html"
    model = File
    table_class = FileTable
    filterset_class = FileFilter

    def get_context_data(self, **kwargs):
        """Provide the context data for the view.

        Returns:
            Dictionary of context data.
        """
        context = super(FileList, self).get_context_data(**kwargs)
        context["unknown_licences"] = File.objects.filter(licence__name="Unknown").count()
        return context


class FileDetailView(LoginRequiredMixin, DetailView):
    """View for a file."""

    model = File


class FileCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """View for creating a glossary definition."""

    model = File
    form_class = FileForm
    template_name = "files/file_form_create.html"
    success_message = "File created!"
    success_url = reverse_lazy("files:file_list")


class FileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """View for updating a glossary definition."""

    model = File
    form_class = FileForm
    template_name = "files/file_form_update.html"
    success_message = "File updated!"
    success_url = reverse_lazy("files:file_list")
