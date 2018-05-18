"""Admin configuration for the pikau application."""

from django.contrib import admin
from django.shortcuts import render
from pikau.models import (
    Level,
    Milestone,
    PikauCourse,
    ProgressOutcome,
    Tag,
    Topic,
    STATUS_CHOICES,
)


class PikauCourseAdmin(admin.ModelAdmin):
    """Admin configuration of Pikau Course pages."""

    list_display = ("name", "language", "status", "readiness_level", "topic", "level")
    filter_horizontal = ("tags", "progress_outcomes", "prerequisites")
    actions = ["update_status"]

    def update_status(self, request, queryset):
        return render(request, "admin/status_intermediate.html", context={})
        context["status_stages"] = STATUS_CHOICES

    def update_status(self, request, queryset):
        # All requests here will actually be of type POST
        # so we will need to check for our special key 'apply'
        # rather than the actual request type.
        print(request.POST, queryset)
        if "new_status" in request.POST:
            queryset.update(status=new_status)
            self.message_user(
                request,
                "Changed status on {} pīkau".format(queryset.count())
            )
            return HttpResponseRedirect(request.get_full_path())
        return render(request, "admin/status_intermediate.html", context={"status_stages": STATUS_CHOICES})

    update_status.short_description = "Update course status"


admin.site.register(PikauCourse, PikauCourseAdmin)
admin.site.register(Level)
admin.site.register(Milestone)
admin.site.register(ProgressOutcome)
admin.site.register(Tag)
admin.site.register(Topic)
