"""Admin configuration for the pikau application."""

from django.contrib import admin

from .models import PikauCourse

class PikauCourseAdmin(admin.ModelAdmin):
    list_display = ("name", "language", "topic", "level")
    filter_horizontal = ("tags", "progress_outcomes")

admin.site.register(PikauCourse, PikauCourseAdmin)
