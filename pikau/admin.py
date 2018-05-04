"""Admin configuration for the pikau application."""

from django.contrib import admin

from .models import PikauCourse

class PikauCourseAdmin(admin.ModelAdmin):
    list_display = ("name", "language", "topic", "level")
    fieldsets = [
        (
            None,
            {"fields": [
                "name",
                "slug",
            ]}
        ),
        (
            "Metadata",
            {"fields": [
                "language",
                "topic",
                "level",
                "tags",
            ]}
        ),
        (
            "Development Information",
            {"fields": [
                "development_folder",
                "status",
                "status_updated",
            ]}
        ),
    ]
    filter_horizontal = ("tags", )
    readonly_fields = ("status_updated", )

admin.site.register(PikauCourse, PikauCourseAdmin)
