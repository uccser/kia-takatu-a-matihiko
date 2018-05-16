"""Views for the pikau application."""

from django.views import generic
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from pikau.models import (
    GlossaryTerm,
    Goal,
    Level,
    PikauCourse,
    PikauUnit,
    ProgressOutcome,
    Tag,
    Topic,
    STATUS_CHOICES,
    READINESS_LEVELS,
)
from pikau.utils import pathways

NUMBER_OF_FLAME_STAGES = 7


class IndexView(LoginRequiredMixin, generic.TemplateView):
    """View for the pikau homepage that renders from a template."""

    template_name = "pikau/index.html"


class DocumentationView(LoginRequiredMixin, generic.TemplateView):
    """View for the pikau documentation that renders from a template."""

    template_name = "pikau/documentation.html"

    def get_context_data(self, **kwargs):
        """Provide the context data for the view.

        Returns:
            Dictionary of context data.
        """
        context = super(DocumentationView, self).get_context_data(**kwargs)
        context["status_stages"] = STATUS_CHOICES
        context["topics"] = Topic.objects.order_by("name")
        context["levels"] = Level.objects.order_by("name")
        context["progress_outcomes"] = ProgressOutcome.objects.order_by("name")
        return context


class GlossaryList(LoginRequiredMixin, generic.ListView):
    """View for the glossary list page."""

    template_name = "pikau/glossary.html"
    context_object_name = "glossary_terms"
    model = GlossaryTerm
    ordering = "term"


class GoalList(LoginRequiredMixin, generic.ListView):
    """View for the goal list page."""

    context_object_name = "goals"
    model = Goal
    ordering = "slug"


class LevelList(LoginRequiredMixin, generic.ListView):
    """View for the level list page."""

    context_object_name = "levels"
    model = Level
    ordering = "name"


class LevelDetail(LoginRequiredMixin, generic.DetailView):
    """View for a level."""

    context_object_name = "level"
    model = Level


class PathwaysView(LoginRequiredMixin, generic.TemplateView):
    """View for the pikau pathway that renders from a template."""

    template_name = "pikau/pathways.html"

    def get_context_data(self, **kwargs):
        """Provide the context data for the pathways view.

        Returns:
            Dictionary of context data.
        """
        context = super().get_context_data(**kwargs)
        context["notation"] = pathways.create_pathways_notation()
        context["readiness_levels"] = READINESS_LEVELS
        return context


class PikauCourseList(LoginRequiredMixin, generic.ListView):
    """View for the pīkau course list page."""

    context_object_name = "pikau_courses"

    def get_queryset(self):
        """Get queryset of all pīkau courses.

        Returns:
            Queryset of ordered PikauCourse objects.
        """
        return PikauCourse.objects.order_by(
            F("milestone").asc(nulls_last=True),
            "readiness_level",
            "name"
        )


class PikauCourseDetail(LoginRequiredMixin, generic.DetailView):
    """View for a pīkau course."""

    context_object_name = "pikau_course"
    model = PikauCourse


class PikauCourseContent(LoginRequiredMixin, generic.DetailView):
    """View for a pīkau course's content."""

    context_object_name = "pikau_course"
    model = PikauCourse
    template_name = "pikau/pikaucourse_content.html"


class PikauUnitDetail(LoginRequiredMixin, generic.DetailView):
    """View for a pīkau unit."""

    context_object_name = "pikau_unit"
    model = PikauUnit

    def get_object(self, **kwargs):
        """Retrieve object for the pīkau unit view.

        Returns:
            PikauUnit object, or raises 404 error if not found.
        """
        return get_object_or_404(
            self.model.objects,
            pikau_course__slug=self.kwargs.get("course_slug", None),
            slug=self.kwargs.get("unit_slug", None)
        )

    def get_context_data(self, **kwargs):
        """Provide the context data for the pikau unit view.

        Returns:
            Dictionary of context data.
        """
        context = super(PikauUnitDetail, self).get_context_data(**kwargs)
        try:
            context["previous_unit"] = PikauUnit.objects.get(
                pikau_course=self.object.pikau_course,
                number=self.object.number - 1
            )
        except ObjectDoesNotExist:
            context["previous_unit"] = None
        try:
            context["next_unit"] = PikauUnit.objects.get(
                pikau_course=self.object.pikau_course,
                number=self.object.number + 1
            )
        except ObjectDoesNotExist:
            context["next_unit"] = None
        return context


class ProgressOutcomeList(LoginRequiredMixin, generic.ListView):
    """View for the progress outcome list page."""

    context_object_name = "progress_outcomes"

    def get_queryset(self):
        """Get queryset of all progress outcomes.

        Returns:
            Queryset of ProgressOutcome objects ordered by name.
        """
        return ProgressOutcome.objects.order_by("name")

    def get_context_data(self, **kwargs):
        """Provide the context data for the view.

        Returns:
            Dictionary of context data.
        """
        context = super(ProgressOutcomeList, self).get_context_data(**kwargs)
        topics = Topic.objects.order_by("name")
        context["topics"] = topics
        max_count = NUMBER_OF_FLAME_STAGES
        for progress_outcome in self.object_list:
            topic_counts = dict()
            for topic in topics:
                count = progress_outcome.pikau_courses.filter(topic=topic).count()
                topic_counts[topic.slug] = dict()
                topic_counts[topic.slug]["count"] = count
                if count > max_count:
                    max_count = count
            progress_outcome.topic_counts = topic_counts
        # Create ranges of heatmap
        stages = list()
        range_width = max_count / NUMBER_OF_FLAME_STAGES
        for num in range(0, NUMBER_OF_FLAME_STAGES):
            stages.append(round(range_width * num, 1))
        stages.append(max_count)
        # Match counts with ranges
        for progress_outcome in self.object_list:
            for topic in topics:
                count = progress_outcome.topic_counts[topic.slug]["count"]
                if count == 0:
                    stage = 0
                elif count == max_count:
                    stage = NUMBER_OF_FLAME_STAGES
                else:
                    found = False
                    i = 0
                    while found is False:
                        stage = i
                        if count < stages[i + 1]:
                            found = True
                        i += 1
                progress_outcome.topic_counts[topic.slug]["stage"] = stage
        return context


class ProgressOutcomeDetail(LoginRequiredMixin, generic.DetailView):
    """View for a progress outcome."""

    context_object_name = "progress_outcome"
    model = ProgressOutcome


class ReadinessLevelList(LoginRequiredMixin, generic.TemplateView):
    """View for the readiness level list page."""

    template_name = "pikau/readiness_level_list.html"

    def get_context_data(self, **kwargs):
        """Provide the context data for the readiness level list view.

        Returns:
            Dictionary of context data.
        """
        context = super().get_context_data(**kwargs)
        readiness_levels = READINESS_LEVELS.copy()
        for level_num, level_data in readiness_levels.items():
            level_data["count"] = PikauCourse.objects.filter(readiness_level=level_num).count()
        context["readiness_levels"] = readiness_levels
        return context


class ReadinessLevelDetail(LoginRequiredMixin, generic.TemplateView):
    """View for a readiness level."""

    template_name = "pikau/readiness_level_detail.html"

    def get_context_data(self, **kwargs):
        """Provide the context data for the readiness level view.

        Returns:
            Dictionary of context data.
        """
        context = super().get_context_data(**kwargs)
        level_number = self.kwargs.get("level_number", 0)
        try:
            readiness_level = READINESS_LEVELS[level_number]
        except KeyError:
            raise Http404("Readiness level does not exist")
        readiness_level["pikau_courses"] = PikauCourse.objects.filter(readiness_level=level_number)
        context["readiness_level"] = readiness_level
        return context


class TagList(LoginRequiredMixin, generic.ListView):
    """View for the tag list page."""

    context_object_name = "tags"
    model = Tag
    ordering = "name"


class TagDetail(LoginRequiredMixin, generic.DetailView):
    """View for a tag."""

    context_object_name = "tag"
    model = Tag


class TopicList(LoginRequiredMixin, generic.ListView):
    """View for the topic list page."""

    context_object_name = "topics"
    model = Topic
    ordering = "name"


class TopicDetail(LoginRequiredMixin, generic.DetailView):
    """View for a topic."""

    context_object_name = "topic"
    model = Topic
