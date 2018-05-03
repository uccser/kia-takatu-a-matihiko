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
    # eg: /pikau//
    path(
        "",
        views.IndexView.as_view(),
        name="index"
    ),
    # eg: /pikau/glossary/
    path(
        "glossary/",
        views.GlossaryList.as_view(),
        name="glossary"
    ),
    # eg: /pikau/goals/
    path(
        "goals/",
        views.GoalList.as_view(),
        name="goal_list"
    ),
    # eg: /pikau/levels/
    path(
        "levels/",
        views.LevelList.as_view(),
        name="level_list"
    ),
    # eg: /pikau/pikau-courses/
    path(
        "pikau-courses/",
        views.PikauCourseList.as_view(),
        name="pikau_course_list"
    ),
    # eg: /pikau/pikau-courses/pikau-1/
    path(
        "pikau-courses/<slug:slug>/",
        views.PikauCourseDetail.as_view(),
        name="pikau_course"
    ),
    # eg: /pikau/progress-outcomes/
    path(
        "progress-outcomes/",
        views.ProgressOutcomeList.as_view(),
        name="progress_outcome_list"
    ),
    # eg: /pikau/tags/
    path(
        "tags/",
        views.TagList.as_view(),
        name="tag_list"
    ),
    # eg: /pikau/topics/
    path(
        "topics/",
        views.TopicList.as_view(),
        name="topic_list"
    ),
]
