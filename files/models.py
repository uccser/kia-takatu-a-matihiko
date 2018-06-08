"""Models for the files application."""

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.urls import reverse

VIDEO_PROVIDERS = (
    "youtube",
    "vimeo",
)

IMAGE_EXTENSIONS = (
    ".jpeg",
    ".jpg",
    ".png",
    ".gif",
    ".svg",
)


def default_licence():
    """Return default licence object.

    Returns:
        Licence 'Unknown' if available, otherwise None.
    """
    try:
        default = Licence.objects.get(slug="unknown").pk
    except ObjectDoesNotExist:
        default = None
    return default


class Licence(models.Model):
    """Model for licence."""

    slug = models.SlugField(unique=True)
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Name",
    )
    url = models.URLField()

    class Meta:
        """Set consistent ordering of licences."""

        ordering = ("name", )

    def get_absolute_url(self):
        """Return the URL for a licence.

        Returns:
            URL as string.
        """
        return self.url

    def __str__(self):
        """Text representation of Licence object.

        Returns:
            String describing licence.
        """
        return self.name


class File(models.Model):
    """Model for file."""

    slug = models.SlugField(unique=True)
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Name",
    )
    filename = models.CharField(max_length=200,
        unique=True,
        verbose_name="Filename",
    )
    location = models.URLField(verbose_name="Location")
    direct_link = models.URLField(blank=True)
    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )
    licence = models.ForeignKey(
        Licence,
        on_delete=models.CASCADE,
        related_name="files",
        default=default_licence,
        null=True,
    )

    def media_type(self):
        """Return label for media type.

        Returns:
            String label of media type.
        """
        if any(substring in self.direct_link for substring in VIDEO_PROVIDERS):
            label = "Video"
        elif self.direct_link.endswith(IMAGE_EXTENSIONS):
            label = "Image"
        else:
            label = "Unknown"
        return label

    def preview_html(self):
        """Return HTML for preview.

        Returns:
            HTML as a string.
        """
        # YouTube video
        if "youtube" in self.direct_link:
            context = {"direct_link": self.direct_link}
            html = render_to_string("files/previews/youtube.html", context=context)
        # Vimeo video
        elif "vimeo" in self.direct_link:
            context = {"video_id": self.direct_link.split("/")[3]}
            html = render_to_string("files/previews/vimeo.html", context=context)
        # Direct image URL
        elif self.direct_link.startswith("http"):
            context = {"direct_link": self.direct_link}
            html = render_to_string("files/previews/external-image.html", context=context)
        # Relative image
        elif self.direct_link:
            context = {"direct_link": self.direct_link}
            html = render_to_string("files/previews/internal-image.html", context=context)
        # Unsupported preview
        else:
            html = "No preview available"
        return html

    def get_absolute_url(self):
        """Return the URL for a file.

        Returns:
            URL as string.
        """
        return reverse("files:file_detail", args=[self.slug])

    def __str__(self):
        """Text representation of File object.

        Returns:
            String describing file.
        """
        return self.name

    def __repr__(self):
        """Text representation of File object for developers.

        Returns:
            String describing file.
        """
        return "File: {}".format(self.slug)
