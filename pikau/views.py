"""Views for the pikau application."""

from django.views import generic
from pikau.models import (
    GlossaryTerm,
    Goal,
    Level,
    PikauCourse,
    ProgressOutcome,
    Tag,
    Topic,
)


class IndexView(generic.TemplateView):
    """View for the pikau homepage that renders from a template."""

    template_name = "pikau/index.html"


class GlossaryList(generic.ListView):
    """View for the glossary list page."""

    template_name = "pikau/glossary.html"
    context_object_name = "glossary_terms"
    model = GlossaryTerm
    ordering = "term"


class GoalList(generic.ListView):
    """View for the goal list page."""

    context_object_name = "goals"
    model = Goal
    ordering = "slug"


class LevelList(generic.ListView):
    """View for the level list page."""

    context_object_name = "levels"
    model = Level
    ordering = "name"


class PikauCourseList(generic.ListView):
    """View for the pīkau course list page."""

    context_object_name = "pikau_courses"
    model = PikauCourse
    ordering = "name"


class PikauCourseDetail(generic.DetailView):
    """View for the pīkau course detail page."""

    context_object_name = "pikau_course"
    model = PikauCourse


class ProgressOutcomeList(generic.ListView):
    """View for the progress outcome list page."""

    context_object_name = "progress_outcomes"
    model = ProgressOutcome
    ordering = "name"


class TagList(generic.ListView):
    """View for the tag list page."""

    context_object_name = "tags"
    model = Tag
    ordering = "name"


class TopicList(generic.ListView):
    """View for the topic list page."""

    context_object_name = "topics"
    model = Topic
    ordering = "name"
