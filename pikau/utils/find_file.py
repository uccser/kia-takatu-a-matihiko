"""Find file object for given filename or slug."""

from os.path import basename
from django.core.exceptions import ObjectDoesNotExist
from files.models import File


def find_file(filename=None, slug=None):
    """Find file object for given filename or slug.

    Args:
        filename (str): String of file filename.
        slug (str): String of file slug.

    Returns:
        File object.

    Raises:
        ValueError: If file object cannot be found.
    """
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
