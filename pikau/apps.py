"""Application configuration for the pikau application."""

from django.apps import AppConfig


class PikauConfig(AppConfig):
    """Configuration object for the pikau application."""

    name = "pikau"

    def ready(self):
        import pikau.signals
