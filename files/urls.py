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
    # eg: /files/
    path(
        "",
        views.FileList.as_view(),
        name="file_list"
    ),
    # eg: /files/file/view/file-1/
    path(
        "file/view/<slug:slug>/",
        views.FileDetailView.as_view(),
        name="file_detail"
    ),
    # eg: /files/file/create/
    path(
        "file/create/",
        views.FileCreateView.as_view(),
        name="file_create"
    ),
    # eg: /files/file/update/file-1/
    path(
        "file/update/<slug:slug>/",
        views.FileUpdateView.as_view(),
        name="file_update"
    ),
    # eg: /files/export/csv/
    path(
        "export/csv/",
        views.file_list_csv,
        name="file_list_export_csv"
    ),
]
