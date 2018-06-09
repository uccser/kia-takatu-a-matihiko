"""Tables for the files application."""

from django.template.loader import render_to_string
import django_tables2 as tables
from files.models import (
    File,
    ProjectItem,
)


class FileTable(tables.Table):
    """Table to display all files."""

    name = tables.LinkColumn()
    preview = tables.TemplateColumn(
        template_name="files/previews/preview.html",
        verbose_name="Preview",
    )
    media_type_rendered = tables.TemplateColumn(
        template_name="files/previews/type-icon.html",
        verbose_name="Media type",
    )
    licence = tables.RelatedLinkColumn()

    def render_media_type(self, value):
        """Render template for media type column.

        Args:
            value: Value for column.

        Returns:
            Rendered string for column.
        """
        if value in ("Image", "Video"):
            context = {"image_path": "images/icons/icons8/{}.png".format(value)}
            image = render_to_string("files/previews/type-icon.html", context=context)
            value = image + value
        return value

    class Meta:
        """Meta attributes for FileTable class."""

        model = File
        fields = ("name", "media_type_rendered", "licence")
        order_by = "name"


class ProjectItemTable(tables.Table):
    """Table to display all project items."""

    name = tables.LinkColumn()

    class Meta:
        """Meta attributes for ProjectItemTable class."""

        model = ProjectItem
        fields = ("name", )
        order_by = "name"
