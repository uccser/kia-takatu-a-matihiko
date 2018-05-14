"""Create test data for pikau tests."""

import os.path
import yaml

from pikau.models import (
    PikauCourse,
)


class PikauTestDataGenerator:
    """Class for generating test data for pikau."""

    def __init__(self):
        """Create PikauTestDataGenerator object."""
        self.BASE_PATH = "tests/pikau/"
        self.LOADER_ASSET_PATH = os.path.join(self.BASE_PATH, "loaders/assets/")

    def load_yaml_file(self, yaml_file_path):
        """Load a yaml file.

        Args:
            yaml_file_path:  The path to a given yaml file (str).

        Returns:
            Contents of a yaml file.
        """
        yaml_file = open(yaml_file_path, encoding="UTF-8").read()
        return yaml.load(yaml_file)

    def create_pikau_course(self, number):
        """Create pikau course object.

        Args:
            number: Identifier of the pikau (int).

        Returns:
            PikauCourse object.
        """
        pikau_course = PikauCourse(
            slug="pikau-course-{}".format(number),
            name="Pikau Course {}".format(number),
            language="en",
        )
        pikau_course.save()
        return pikau_course
