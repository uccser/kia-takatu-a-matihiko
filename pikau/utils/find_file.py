""""""

from os.path import basename
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from files.models import File


def find_file(filename=None, slug=None):
    if not filename and not slug:
        raise ValueError("One keyword argument is required: filename or slug")
    try:
        if filename:
            file_object = File.objects.get(filename=filename)
        else:
            file_object = File.objects.get(slug=slug)
    except ObjectDoesNotExist:
        if filename and not filename.startswith("http"):
            try:
                filename = basename(filename)
                file_object = File.objects.get(filename=filename)
            except ObjectDoesNotExist:
                file_object = None
        else:
            file_object = None
    if not file_object:
        raise ValueError("File '{}' not listed in files list".format(filename or slug))
    else:
        return file_object
