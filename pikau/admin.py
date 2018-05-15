"""Admin configuration for the pikau application."""

from django.contrib import admin
from pikau.models import (
    Level,
    Milestone,
    PikauCourse,
    ProgressOutcome,
    Tag,
    Topic,
)


class PikauCourseAdmin(admin.ModelAdmin):
    list_display = ("name", "language", "topic", "level")
    filter_horizontal = ("tags", "progress_outcomes", "prerequisites")


admin.site.register(PikauCourse, PikauCourseAdmin)
admin.site.register(Level)
admin.site.register(Milestone)
admin.site.register(ProgressOutcome)
admin.site.register(Tag)
admin.site.register(Topic)
