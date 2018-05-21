"""Mixins for pikau application."""

from django.contrib import messages


class SuccessMessageDeleteMixin(object):

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class GlossaryActionMixin(object):
    """Sets fields for pages relating to actions of glossary items."""

    fields = ("term", "description", "slug")


# class MilestoneActionMixin(SuccessMessageMixin):
#
#     fields = ("name", "date")


# class GoalActionMixin(SuccessMessageMixin):
#
#     fields = ("description", "slug")


# class TagActionMixin(SuccessMessageMixin):
#
#     fields = ("name", "description", "slug")
#

class TopicActionMixin(object):

    fields = ("name", "slug")


# class LevelActionMixin(SuccessMessageMixin):
#
#     fields = ("name", "slug")
