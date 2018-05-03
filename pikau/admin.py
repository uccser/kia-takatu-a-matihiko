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
                "language",
            ]}
        ),
        (
            "Development Information",
            {"fields": [
                "topic",
                "level",
                "tags",
            ]}
        ),
    ]
    filter_horizontal = ("tags", )

admin.site.register(PikauCourse, PikauCourseAdmin)
