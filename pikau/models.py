"""Models for the pikau application."""

from django.db import models


class GlossaryTerm(models.Model):
    """Model for glossary term."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    term = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        """Text representation of GlossaryTerm object.

        Returns:
            String describing GlossaryTerm.
        """
        return self.term


class Goal(models.Model):
    """Model for goal."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
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
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, unique=True)

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
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200, unique=True)
    language = models.CharField(max_length=20)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="pikau_courses"
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        related_name="pikau_courses"
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="pikau_courses",
    )
    glossary_terms = models.ManyToManyField(
        GlossaryTerm,
        related_name="pikau_courses",
    )
    trailer_video = models.URLField()
    cover_photo = models.CharField(max_length=100)
    overview = models.TextField()
    study_plan = models.TextField()
    assessment_description = models.TextField()
    assessment_items = models.TextField()
    # TODO: Add resources
    # TODO: Add content

    def __str__(self):
        """Text representation of PikauCourse object.

        Returns:
            String describing PikauCourse.
        """
        return self.name
