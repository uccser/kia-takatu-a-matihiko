"""Create test data for pikau tests."""

import os.path

from files.models import (
    File,
    Licence
)


class FileTestDataGenerator:
    """Class for generating test data for pikau."""

    def __init__(self):
        """Create PikauTestDataGenerator object."""
        self.BASE_PATH = "tests/pikau/"
        self.LOADER_ASSET_PATH = os.path.join(self.BASE_PATH, "loaders/assets/")

    def create_file(self, number, licence=None):
        """Create file object.

        Args:
            number: Identifier of the file (int).

        Returns:
            File object.
        """
        file_object = File(
            slug="file-{}".format(number),
            name="File {}".format(number),
            filename="file-{}.ext".format(number),
            description="Description for file {}".format(number),
            location="https://www.example.com/{}".format(number),
        )
        file_object.save()
        if licence:
            file_object.licence.add(licence)
        return file_object

    def create_licence(self, number):
        """Create licence object.

        Args:
            number: Identifier of the file (int).

        Returns:
            File object.
        """
        licence = Licence(
            slug="licence-{}".format(number),
            name="Licence {}".format(number),
            url="https://www.example.com/licence-{}".format(number),
        )
        licence.save()
        return licence
