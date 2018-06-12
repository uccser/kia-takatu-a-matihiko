"""Admin configuration for the files application."""

from django.contrib import admin
from files.models import (
    File,
    Licence,
    ProjectItem,
)


admin.site.register(File)
admin.site.register(Licence)
admin.site.register(ProjectItem)
