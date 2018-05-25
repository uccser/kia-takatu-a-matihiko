"""Create test data for pikau tests."""

import os.path
import yaml

from pikau.models import (
    PikauCourse,
    GlossaryTerm,
    Goal,
    Tag,
    Topic,
    Level,
    ProgressOutcome,
    Milestone,
    PikauUnit,
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

    def create_glossary_term(self, number):
        """Create GlossaryTerm object.

        Args:
            number: Identifier of the glossary term (int).

        Returns:
            GlossaryTerm object.
        """
        glossary_term = GlossaryTerm(
            slug="glossary-term-{}".format(number),
            term="Glossary Term {}".format(number),
            description="<p>Description for glossary term {}.</p>".format(number),
        )
        glossary_term.save()
        return glossary_term

    def create_goal(self, number):
        """Create Goal object.

        Args:
            number: Identifier of the goal (int).

        Returns:
            Goal object.
        """
        goal = Goal(
            slug="goal-{}".format(number),
            description="<p>Description for goal {}.</p>".format(number),
        )
        goal.save()
        return goal

    def create_tag(self, number):
        """Create Tag object.

        Args:
            number: Identifier of the tag (int).

        Returns:
            Tag object.
        """
        tag = Tag(
            slug="tag-{}".format(number),
            name="tag-{}-name".format(number),
            description="<p>Description for tag {}.</p>".format(number),
        )
        tag.save()
        return tag

    def create_topic(self, number):
        """Create Topic object.

        Args:
            number: Identifier of the topic (int).

        Returns:
            Topic object.
        """
        topic = Topic(
            slug="topic-{}".format(number),
            name="topic-{}-name".format(number),
        )
        topic.save()
        return topic

    def create_level(self, number):
        """Create Level object.

        Args:
            number: Identifier of the level (int).

        Returns:
            Level object.
        """
        level = Level(
            slug="level-{}".format(number),
            name="level-{}-name".format(number),
        )
        level.save()
        return level

    def create_progress_outcome(self, number):
        """Create Progress Outcome object.

        Args:
            number: Identifier of the progress outcome (int).

        Returns:
            Progress Outcome object.
        """
        progress_outcome = ProgressOutcome(
            slug="progress-outcome-{}".format(number),
            name="progress-outcome-{}-name".format(number),
            abbreviation="pr-out-{}".format(number),
            description="Description for progress outcome {}.".format(number),
            exemplars="progress-outcome-{}".format(number),
        )
        progress_outcome.save()
        return progress_outcome

    def create_milestone(self, number, date):
        """Create Milestone object.

        Args:
            number: Identifier of the milestone (int).

        Returns:
            Milestone object.
        """
        milestone = Milestone(
            name="milestone-{}".format(number),
            date=date,
        )
        milestone.save()
        return milestone

    def create_pikau_unit(self, pikau_course, number, module_name=False):
        """Create PikauUnit object.

        Args:
            number: Identifier of the pikau unit (int).

        Returns:
            PikauUnit object.
        """
        pikau_unit = PikauUnit(
            slug="pikau-unit-{}".format(number),
            number=number,
            pikau_course=pikau_course,
            name="pikau-unit-{}-name".format(number),
            # module_name="pikau-unit-{}-module-name".format(number),
            content="<p>Content for piaku unit {}.</p>".format(number),
        )
        if module_name:
            pikau_unit.module_name = "pikau-unit-{}-module-name".format(number)

        pikau_unit.save()
        return pikau_unit