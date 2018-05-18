"""Models for the files application."""

from django.db import models


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
        blank=True,
        null=True,
    )

    def __str__(self):
        """Text representation of File object.

        Returns:
            String describing file.
        """
        return self.filename
