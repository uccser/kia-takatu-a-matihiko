"""Views for the pikau application."""

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from pikau.models import (
    GlossaryTerm,
    Goal,
    Level,
    PikauCourse,
    ProgressOutcome,
    Tag,
    Topic,
)

NUMBER_OF_FLAME_STAGES = 7


class IndexView(LoginRequiredMixin, generic.TemplateView):
    """View for the pikau homepage that renders from a template."""

    template_name = "pikau/index.html"


class GlossaryList(LoginRequiredMixin,generic.ListView):
    """View for the glossary list page."""

    template_name = "pikau/glossary.html"
    context_object_name = "glossary_terms"
    model = GlossaryTerm
    ordering = "term"


class GoalList(LoginRequiredMixin,generic.ListView):
    """View for the goal list page."""

    context_object_name = "goals"
    model = Goal
    ordering = "slug"


class LevelList(LoginRequiredMixin,generic.ListView):
    """View for the level list page."""

    context_object_name = "levels"
    model = Level
    ordering = "name"


class LevelDetail(LoginRequiredMixin,generic.DetailView):
    """View for a level."""

    context_object_name = "level"
    model = Level


class PikauCourseList(LoginRequiredMixin,generic.ListView):
    """View for the pīkau course list page."""

    context_object_name = "pikau_courses"
    model = PikauCourse
    ordering = "name"


class PikauCourseDetail(LoginRequiredMixin,generic.DetailView):
    """View for a pīkau course."""

    context_object_name = "pikau_course"
    model = PikauCourse


class ProgressOutcomeList(LoginRequiredMixin,generic.ListView):
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
                    while found == False:
                        stage = i
                        if count < stages[i + 1]:
                            found = True
                        i += 1
                progress_outcome.topic_counts[topic.slug]["stage"] = stage
        return context


class ProgressOutcomeDetail(LoginRequiredMixin,generic.DetailView):
    """View for a progress outcome."""

    context_object_name = "progress_outcome"
    model = ProgressOutcome


class TagList(LoginRequiredMixin,generic.ListView):
    """View for the tag list page."""

    context_object_name = "tags"
    model = Tag
    ordering = "name"


class TagDetail(LoginRequiredMixin,generic.DetailView):
    """View for a tag."""

    context_object_name = "tag"
    model = Tag


class TopicList(LoginRequiredMixin,generic.ListView):
    """View for the topic list page."""

    context_object_name = "topics"
    model = Topic
    ordering = "name"


class TopicDetail(LoginRequiredMixin,generic.DetailView):
    """View for a topic."""

    context_object_name = "topic"
    model = Topic
