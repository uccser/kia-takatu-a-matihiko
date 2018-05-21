"""Models for the files application."""

from django.db import models
from django.core.exceptions import ObjectDoesNotExist


def default_licence():
    """Return default licence object.

    Returns:
        Licence 'Unknown' if available, otherwise None.
    """
    try:
        default = Licence.objects.get(name="Unknown").pk
    except ObjectDoesNotExist:
        default = None
    return default


class Licence(models.Model):
    """Model for licence."""

    name = models.CharField(max_length=200, unique=True)
    url = models.URLField()

    class Meta:
        """Set consistent ordering of licences."""

        ordering = ("name", )

    def __str__(self):
        """Text representation of Licence object.

        Returns:
            String describing licence.
        """
        return self.name


class File(models.Model):
    """Model for file."""

    slug = models.SlugField(unique=True)
    filename = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.URLField()
    licence = models.ForeignKey(
        Licence,
        on_delete=models.CASCADE,
        related_name="files",
        default=default_licence,
    )

    def __str__(self):
        """Text representation of File object.

        Returns:
            String describing file.
        """
        return self.filename

    def __repr__(self):
        """Text representation of File object for developers.

        Returns:
            String describing file.
        """
        return "File: {}".format(self.slug)
