"""Mixins for pikau application."""

from django.contrib import messages


class SuccessMessageDeleteMixin(object):
    """Allow success message for delete view."""

    def delete(self, request, *args, **kwargs):
        """Set success string in message."""
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class TopicActionMixin(object):
    """Topic mixin."""

    fields = ("name", "slug")
