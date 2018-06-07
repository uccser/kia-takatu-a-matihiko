"""Tables for the files application."""

from django.template.loader import render_to_string
import django_tables2 as tables
from files.models import (
    File,
)


class FileTable(tables.Table):
    """Table to display all files."""

    name = tables.LinkColumn()
    media_type_rendered = tables.TemplateColumn(
        template_name="files/previews/type-icon.html",
        verbose_name="Media type",
    )
    licence = tables.RelatedLinkColumn()

    def render_media_type(self, value):
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
