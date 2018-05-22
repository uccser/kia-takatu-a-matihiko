"""URL routing for the pikau application.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = "pikau"

urlpatterns = [
    # eg: /pikau/
    path(
        "",
        views.IndexView.as_view(),
        name="index"
    ),
    # eg: /pikau/docs/
    path(
        "docs/",
        views.DocumentationView.as_view(),
        name="docs"
    ),
    # eg: /pikau/glossary/
    path(
        "glossary/",
        views.GlossaryListView.as_view(),
        name="glossaryterm_list"
    ),
    # eg: /pikau/glossary/view/slug-1/
    path(
        "glossary/view/<slug:slug>",
        views.GlossaryDetailView.as_view(),
        name="glossaryterm_detail"
    ),
    # eg: /pikau/glossary/create/
    path(
        "glossary/create/",
        views.GlossaryCreateView.as_view(),
        name="glossaryterm_create"
    ),
    # eg: /pikau/glossary/update/term-1/
    path(
        "glossary/update/<slug:slug>/",
        views.GlossaryUpdateView.as_view(),
        name="glossaryterm_update"
    ),
    # eg: /pikau/glossary/delete/term-1/
    path(
        "glossary/delete/<slug:slug>/",
        views.GlossaryDeleteView.as_view(),
        name="glossaryterm_delete"
    ),
    # eg: /pikau/goals/
    path(
        "goals/",
        views.GoalListView.as_view(),
        name="goal_list"
    ),
    # eg: /pikau/levels/
    path(
        "levels/",
        views.LevelListView.as_view(),
        name="level_list"
    ),
    # eg: /pikau/levels/level-1/
    path(
        "levels/<slug:slug>/",
        views.LevelDetailView.as_view(),
        name="level"
    ),
    # eg: /pikau/milestones/
    path(
        "milestones/",
        views.MilestoneListView.as_view(),
        name="milestone_list"
    ),
    # eg: /pikau/milestones/1/
    path(
        "milestones/<int:pk>/",
        views.MilestoneDetailView.as_view(),
        name="milestone"
    ),
    # eg: /pikau/pathways/
    path(
        "pathways/",
        views.PathwaysView.as_view(),
        name="pathways"
    ),
    # eg: /pikau/pikau-courses/
    path(
        "pikau-courses/",
        views.PikauCourseListView.as_view(),
        name="pikau_course_list"
    ),
    # eg: /pikau/pikau-courses/pikau-1/
    path(
        "pikau-courses/<slug:slug>/",
        views.PikauCourseDetailView.as_view(),
        name="pikau_course"
    ),
    # eg: /pikau/pikau-courses/pikau-1/content/
    path(
        "pikau-courses/<slug:slug>/content/",
        views.PikauCourseContentView.as_view(),
        name="pikau_content"
    ),
    # eg: /pikau/pikau-courses/pikau-1/content/unit-1/
    path(
        "pikau-courses/<slug:course_slug>/content/<slug:unit_slug>/",
        views.PikauUnitDetailView.as_view(),
        name="pikau_unit"
    ),
    # eg: /pikau/progress-outcomes/
    path(
        "progress-outcomes/",
        views.ProgressOutcomeListView.as_view(),
        name="progress_outcome_list"
    ),
    # eg: /pikau/progress-outcomes/progress-outcome-1/
    path(
        "progress-outcomes/<slug:slug>/",
        views.ProgressOutcomeDetailView.as_view(),
        name="progress_outcome"
    ),
    # eg: /pikau/readiness-levels/
    path(
        "readiness-levels/",
        views.ReadinessLevelListView.as_view(),
        name="readiness_level_list"
    ),
    # eg: /pikau/readiness-levels/1/
    path(
        "readiness-levels/<int:level_number>/",
        views.ReadinessLevelDetailView.as_view(),
        name="readiness_level"
    ),
    # eg: /pikau/tags/
    path(
        "tags/",
        views.TagListView.as_view(),
        name="tag_list"
    ),
    # eg: /pikau/tags/tag-1/
    path(
        "tags/<slug:slug>/",
        views.TagDetailView.as_view(),
        name="tag"
    ),
    # eg: /pikau/topics/
    path(
        "topics/",
        views.TopicListView.as_view(),
        name="topic_list"
    ),
    # eg: /pikau/topics/topic-1/
    path(
        "topics/view/<slug:slug>/",
        views.TopicDetailView.as_view(),
        name="topic"
    ),
    # eg: /pikau/topics/create/
    path(
        "topics/create/",
        views.TopicCreateView.as_view(),
        name="topic_create"
    ),
    # eg: /pikau/topics/update/topic-1/
    path(
        "topics/update/<slug:slug>/",
        views.TopicUpdateView.as_view(),
        name="topic_update"
    ),
    # eg: /pikau/topics/delete/topic-1/
    path(
        "topics/delete/<slug:slug>/",
        views.TopicDeleteView.as_view(),
        name="topic_delete"
    ),
]
