"""Views for the files application."""

import csv
from django.http import HttpResponse
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

    def get_context_data(self, **kwargs):
        """Provide the context data for the view.

        Returns:
            Dictionary of context data.
        """
        context = super(FileDetailView, self).get_context_data(**kwargs)
        context["table"] = ProjectItemTable(self.object.project_items.all())
        context["attribution_text"] = self.object.attribution()
        context["attribution_html"] = self.object.attribution(html=True)
        return context


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
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="ktam_file_licence_data_{datetime}.csv"'.format(datetime=1)
    writer = csv.writer(response)

    files = File.objects.order_by(
        "title",
        "project_items__name",
    )
    writer.writerow(
        [
            "Title",
            "Author",
            "Location",
            "Filename",
            "Description",
            "Licence",
            "Attribution (Text)",
            "Attribution (HTML)",
            "Used in item",
        ]
    )
    for file_obj in files:
        if file_obj.project_items.exists():
            for project_item in file_obj.project_items.order_by("name"):
                writer.writerow(
                    [
                        file_obj.title,
                        file_obj.author,
                        file_obj.location,
                        file_obj.filename,
                        file_obj.description,
                        file_obj.licence.name,
                        file_obj.attribution(),
                        file_obj.attribution(html=True),
                        project_item.name,
                    ]
                )
        else:
            writer.writerow(
                [
                    file_obj.title,
                    file_obj.author,
                    file_obj.location,
                    file_obj.filename,
                    file_obj.description,
                    file_obj.licence.name,
                    file_obj.attribution(),
                    file_obj.attribution(html=True),
                ]
            )
    return response


class ProjectItemListView(LoginRequiredMixin, SingleTableMixin, ListView):
    """View for the project item list page."""

    template_name = "files/project_item_list.html"
    model = ProjectItem
    table_class = ProjectItemTable
