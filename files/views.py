"""Views for the files application."""

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    ListView,
)
from files.tables import (
    FileTable,
    ProjectItemTable,
)
from files.filters import FileFilter
from files.models import (
    File,
    ProjectItem,
    default_licence,
)
from files.forms import (
    FileForm,
)
from djqscsv import render_to_csv_response


class IndexView(LoginRequiredMixin, TemplateView):
    """View for the files homepage that renders from a template."""

    template_name = "files/index.html"


class FileListView(LoginRequiredMixin, SingleTableMixin, FilterView):
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
        context = super(FileListView, self).get_context_data(**kwargs)
        context["unknown_licences"] = File.objects.filter(licence__name="Unknown").count()
        context["unknown_licence_id"] = default_licence()
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


def file_list_csv(request):
    """Export all files as CSV.

    Args:
        request (Request): User request.

    Returns:
        CSV response of all files.
    """
    files = File.objects.all().values(
        "name",
        "licence__name",
        "location",
        "filename",
        "description",
    ).order_by(
        "name",
    )
    return render_to_csv_response(
        files,
        append_datestamp=True,
        field_header_map={"licence__name": "Licence"},
        filename="ktam_file_licence_data"
    )


class ProjectItemListView(LoginRequiredMixin, SingleTableMixin, ListView):
    """View for the project item list page."""

    template_name = "files/project_item_list.html"
    model = ProjectItem
    table_class = ProjectItemTable
