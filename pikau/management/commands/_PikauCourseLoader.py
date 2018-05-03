"""Custom loader for loading pikau courses."""

import os.path
from django.db import transaction
from utils.BaseLoader import BaseLoader
from pikau.models import (
    PikauCourse,
    Topic,
    Level,
    Tag,
    GlossaryTerm,
)

CONFIG_FILE = "pikau-courses.yaml"


class PikauCourseLoader(BaseLoader):
    """Custom loader for loading pikau courses."""

    @transaction.atomic
    def load(self):
        """Load the pikau courses into the database."""
        pikau_courses = self.load_yaml_file(CONFIG_FILE)

        for pikau_course_slug in pikau_courses.get("courses", list()):
            self.base_path = os.path.join(self.base_path, "pikau-courses", pikau_course_slug)
            pikau_course_metadata = self.load_yaml_file("metadata.yaml")
            pikau_course_overview = self.convert_md_file(
                pikau_course_metadata["overview"],
                CONFIG_FILE,
                heading_required=False,
                remove_title=False,
            ).html_string
            pikau_course_study_plan = self.convert_md_file(
                pikau_course_metadata["study-plan"],
                CONFIG_FILE,
                heading_required=False,
                remove_title=False,
            ).html_string
            pikau_course_assessment_description = self.convert_md_file(
                pikau_course_metadata["assessment-description"],
                CONFIG_FILE,
                heading_required=False,
                remove_title=False,
            ).html_string
            pikau_course_assessment_items = self.convert_md_file(
                pikau_course_metadata["assessment-items"],
                CONFIG_FILE,
                heading_required=False,
                remove_title=False,
            ).html_string

            pikau_course = PikauCourse(
                slug=pikau_course_slug,
                name=pikau_course_metadata["name"],
                language=pikau_course_metadata["language"],
                topic=Topic.objects.get(slug=pikau_course_metadata["topic"]),
                level=Level.objects.get(slug=pikau_course_metadata["level"]),
                trailer_video=pikau_course_metadata["trailer-video"],
                cover_photo=pikau_course_metadata["cover-photo"],
                overview=pikau_course_overview,
                study_plan=pikau_course_study_plan,
                assessment_description=pikau_course_assessment_description,
                assessment_items=pikau_course_assessment_items,
            )
            pikau_course.save()

            for pikau_course_tag_slug in pikau_course_metadata.get("tags", list()):
                pikau_course.tags.add(Tag.objects.get(slug=pikau_course_tag_slug))

            for pikau_course_glossary_term_slug in pikau_course_metadata.get("glossary", list()):
                pikau_course.glossary_terms.add(GlossaryTerm.objects.get(slug=pikau_course_glossary_term_slug))

            self.log("Added pikau course: {}".format(pikau_course.__str__()))

        self.log("All pikau courses loaded!\n")
