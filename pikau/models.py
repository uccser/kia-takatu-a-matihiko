"""Models for the pikau application."""

from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters
from django.urls import reverse
from files.models import ProjectItem


LANGUAGE_CHOICES = (
    ("en", "English"),
    ("mi", "Māori"),
)

STAGE_1 = (1, "Stage 1: Conceptualising")
STAGE_2 = (2, "Stage 2: Developing")
STAGE_3 = (3, "Stage 3: Reviewing - Academic")
STAGE_4 = (4, "Stage 4: Reviewing - Language")
STAGE_5 = (5, "Stage 5: Reviewing - Technical")
STAGE_6 = (6, "Stage 6: Completed")
STAGE_7 = (7, "Stage 7: Completed - Published to iQualify")

STATUS_CHOICES = (
    STAGE_1,
    STAGE_2,
    STAGE_3,
    STAGE_4,
    STAGE_5,
    STAGE_6,
    STAGE_7,
)

READINESS_LEVELS = {
    1: {"name": "Level 1 - Hika - Ignite", "color": "#ffd742"},
    2: {"name": "Level 2 - Māpura - Spark", "color": "#ffae19"},
    3: {"name": "Level 3 - Hahana - Glow", "color": "#fe9b19"},
    4: {"name": "Level 4 - Muramura - Burn", "color": "#ff623d"},
    5: {"name": "Level 5 - Whitawhita - Blaze", "color": "#ee2522"},
}
READINESS_CHOICES = []
for level_num, level_data in READINESS_LEVELS.items():
    READINESS_CHOICES.append((level_num, level_data["name"]))
READINESS_CHOICES = tuple(READINESS_CHOICES)


class GlossaryTerm(models.Model):
    """Model for glossary term."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(
        unique=True,
        max_length=200,
        help_text="A unique readable identifier",
    )
    term = models.CharField(max_length=200, unique=True)
    definition = models.TextField()

    def get_absolute_url(self):
        """Return the canonical URL for a glossary term.

        Returns:
            URL as string.
        """
        return reverse("pikau:glossaryterm_detail", args=[self.slug])

    def __str__(self):
        """Text representation of GlossaryTerm object.

        Returns:
            String describing GlossaryTerm.
        """
        return self.term


class Milestone(models.Model):
    """Model for milestone."""

    name = models.CharField(max_length=100, unique=True)
    date = models.DateField()

    class Meta:
        """Set consistent ordering of milestones."""

        ordering = ["date", "name"]

    @property
    def is_upcoming(self):
        """Return true if milestone is in future."""
        return self.date > date.today()

    def __str__(self):
        """Text representation of Milestone object.

        Returns:
            String describing Milestone.
        """
        return "{} - {}".format(self.name, defaultfilters.date(self.date))


class Goal(models.Model):
    """Model for goal."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True, max_length=200)
    description = models.CharField(max_length=500, unique=True)

    def __str__(self):
        """Text representation of Goal object.

        Returns:
            String describing Goal.
        """
        return self.description


class Tag(models.Model):
    """Model for tag."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True, max_length=200)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """Text representation of Tag object.

        Returns:
            String describing Tag.
        """
        return self.name


class Topic(models.Model):
    """Model for topic."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        """Return the canonical URL for a topic.

        Returns:
            URL as string.
        """
        return reverse("pikau:topic", args=[self.slug])

    def __str__(self):
        """Text representation of Topic object.

        Returns:
            String describing Topic.
        """
        return self.name


class Level(models.Model):
    """Model for level."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """Text representation of Level object.

        Returns:
            String describing Level.
        """
        return self.name


class ProgressOutcome(models.Model):
    """Model for progress outcome."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    exemplars = models.URLField()

    def __str__(self):
        """Text representation of ProgressOutcome object.

        Returns:
            String describing ProgressOutcome.
        """
        return self.name


class PikauCourse(models.Model):
    """Model for Pikau Course."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True, max_length=200)
    name = models.CharField(max_length=200, unique=True)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    readiness_level = models.IntegerField(
        choices=READINESS_CHOICES,
        default=1,
        null=True,
        blank=True,
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.PROTECT,
        related_name="pikau_courses",
        blank=True,
        null=True,
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.PROTECT,
        related_name="pikau_courses",
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="pikau_courses",
        blank=True,
    )
    progress_outcomes = models.ManyToManyField(
        ProgressOutcome,
        related_name="pikau_courses",
        blank=True,
    )
    glossary_terms = models.ManyToManyField(
        GlossaryTerm,
        related_name="pikau_courses",
        blank=True,
    )
    prerequisites = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="postrequisites",
        blank=True,
    )
    trailer_video = models.URLField(blank=True)
    cover_photo = models.CharField(max_length=100, default="images/core-education/pikau-course-cover.png")
    overview = models.TextField(blank=True)
    study_plan = models.TextField(blank=True)
    assessment_description = models.TextField(blank=True)
    assessment_items = models.TextField(blank=True)
    project_item = models.OneToOneField(
        ProjectItem,
        on_delete=models.SET_NULL,
        related_name="pikau_course",
        blank=True,
        null=True,
    )

    # Development attributes
    development_folder = models.URLField(blank=True)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=1,
    )
    status_updated = models.DateTimeField(null=True)
    __previous_status = None
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="pikau_courses",
        blank=True,
        null=True,
    )
    milestone = models.ForeignKey(
        Milestone,
        on_delete=models.PROTECT,
        related_name="pikau_courses",
        blank=True,
        null=True,
    )

    @property
    def is_overdue_milestone(self):
        """Return true if not completed and past milestone."""
        return self.status < STAGE_6[0] and self.milestone.date < date.today()

    def get_absolute_url(self):
        """Return the canonical URL for a pikau course.

        Returns:
            URL as string.
        """
        return reverse("pikau:pikau_course", args=[self.slug])

    def __str__(self):
        """Text representation of PikauCourse object.

        Returns:
            String describing PikauCourse.
        """
        return self.name


class PikauUnit(models.Model):
    """Model for Pikau Unit."""

    slug = models.SlugField(max_length=200)
    number = models.PositiveSmallIntegerField()
    pikau_course = models.ForeignKey(
        PikauCourse,
        on_delete=models.PROTECT,
        related_name="content"
    )
    name = models.CharField(max_length=200)
    module_name = models.CharField(max_length=200, null=True)
    content = models.TextField()

    def __str__(self):
        """Text representation of PikauUnit object.

        Returns:
            String describing PikauUnit.
        """
        if self.module_name:
            return "{}: {} - {}".format(
                self.pikau_course.name,
                self.module_name,
                self.name,
            )
        else:
            return "{}: {}".format(self.pikau_course.name, self.name)

    class Meta:
        """Set metadata of pikau units."""

        ordering = ["number", ]
        unique_together = (
            ("slug", "pikau_course"),
        )
