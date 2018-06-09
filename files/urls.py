"""URL routing for the files application.

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

app_name = "files"

urlpatterns = [
    # eg: /file-tracking/
    path(
        "",
        views.IndexView.as_view(),
        name="index"
    ),
    # eg: /file-tracking/file/list/
    path(
        "files/list/",
        views.FileListView.as_view(),
        name="file_list"
    ),
    # eg: /file-tracking/file/view/file-1/
    path(
        "files/view/<slug:slug>/",
        views.FileDetailView.as_view(),
        name="file_detail"
    ),
    # eg: /file-tracking/file/create/
    path(
        "files/create/",
        views.FileCreateView.as_view(),
        name="file_create"
    ),
    # eg: /file-tracking/file/update/file-1/
    path(
        "files/update/<slug:slug>/",
        views.FileUpdateView.as_view(),
        name="file_update"
    ),
    # eg: /file-tracking/export/csv/
    path(
        "export/csv/",
        views.file_list_csv,
        name="file_list_export_csv"
    ),
    # # eg: /file-tracking/item/view/item-1/
    path(
        "items/list/",
        views.ProjectItemListView.as_view(),
        name="project_item_list"
    ),
]
