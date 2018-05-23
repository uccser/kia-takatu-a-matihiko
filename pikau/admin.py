"""Admin configuration for the pikau application."""

from django.contrib import admin
from pikau.models import (
    GlossaryTerm,
    Goal,
    Level,
    Milestone,
    PikauCourse,
    PikauUnit,
    ProgressOutcome,
    Tag,
    Topic,
)


class PikauCourseAdmin(admin.ModelAdmin):
    """Admin configuration of Pikau Course pages."""

    list_display = ("name", "language", "status", "readiness_level", "topic", "level")
    filter_horizontal = ("tags", "progress_outcomes", "prerequisites")


admin.site.register(GlossaryTerm)
admin.site.register(Goal)
admin.site.register(Level)
admin.site.register(Milestone)
admin.site.register(ProgressOutcome)
admin.site.register(PikauCourse, PikauCourseAdmin)
admin.site.register(PikauUnit)
admin.site.register(Tag)
admin.site.register(Topic)
