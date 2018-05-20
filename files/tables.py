import django_tables2 as tables
from files.models import (
    File,
)


class FileTable(tables.Table):

    class Meta:
        model = File
        fields = ("filename", "licence")
