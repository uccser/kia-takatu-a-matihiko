import django_filters
from files.models import File


class FileFilter(django_filters.FilterSet):

    class Meta:
        model = File
        fields = ["licence"]
