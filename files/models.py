"""Models for the files application."""

from django.db import models
from django.core.exceptions import ObjectDoesNotExist, ValidationError
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
    filename = models.CharField(
        max_length=200,
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


class ProjectItem(models.Model):
    """Model for project item."""

    ITEM_TYPE_WEBPAGE = 1
    ITEM_TYPE_PIKAU = 20
    ITEM_TYPE_PRINT = 50
    ITEM_TYPE_OTHER = 99
    ITEM_TYPE_CHOICES = (
        (ITEM_TYPE_WEBPAGE, "Webpage"),
        (ITEM_TYPE_PIKAU, "Pīkau"),
        (ITEM_TYPE_PRINT, "Print Media"),
        (ITEM_TYPE_OTHER, "Other"),
    )

    name = models.CharField(
        max_length=300,
        unique=True,
        verbose_name="Name",
    )
    url = models.URLField(
        blank=True,
        verbose_name="Location (URL)",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )
    files = models.ManyToManyField(
        File,
        verbose_name="Files",
        related_name="project_items",
        blank=True,
    )
    item_type = models.PositiveSmallIntegerField(
        choices=ITEM_TYPE_CHOICES,
        default=ITEM_TYPE_OTHER,
        verbose_name="Type",
    )

    def clean(self):
        """Don't allow name to be blank."""
        if not self.name:
            raise ValidationError("Name cannot be empty.")

    def get_absolute_url(self):
        """Return the URL for a project item.

        Returns:
            URL as string.
        """
        if self.url:
            url = self.url
        elif self.pikau_course:
            url = self.pikau_course.get_absolute_url() + "#file-list"
        else:
            url = None
        return url

    def __str__(self):
        """Text representation of project item object.

        Returns:
            String describing project item.
        """
        return self.name

    def __repr__(self):
        """Text representation of project item object for developers.

        Returns:
            String describing project item.
        """
        return "Project item: {}".format(self.name)
