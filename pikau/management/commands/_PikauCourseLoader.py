"""Custom loader for loading pikau courses."""

import os.path
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from utils.BaseLoader import BaseLoader
from pikau.utils.find_file import find_file
from pikau.models import (
    PikauCourse,
    PikauUnit,
    Topic,
    Level,
    Tag,
    GlossaryTerm,
    ProgressOutcome,
)
from files.models import ProjectItem


CONFIG_FILE = "pikau-courses.yaml"
COVER_PHOTO_DEFAULT = "images/core-education/pikau-course-cover.png"


class PikauCourseLoader(BaseLoader):
    """Custom loader for loading pikau courses."""

    @transaction.atomic
    def load(self):
        """Load the pikau courses into the database."""
        pikau_courses = self.load_yaml_file(CONFIG_FILE)
        self.original_base_path = self.base_path

        for pikau_course_slug in pikau_courses.get("courses", list()):
            self.base_path = os.path.join(self.original_base_path, "pikau-courses", pikau_course_slug)
            pikau_course_metadata = self.load_yaml_file("metadata.yaml")
            pikau_course_overview = pikau_course_metadata.get("overview", "")
            if pikau_course_overview:
                pikau_course_overview = self.convert_md_file(
                    pikau_course_metadata["overview"],
                    CONFIG_FILE,
                    heading_required=False,
                    remove_title=False,
                ).html_string
            pikau_course_study_plan = pikau_course_metadata.get("study-plan", "")
            if pikau_course_study_plan:
                pikau_course_study_plan = self.convert_md_file(
                    pikau_course_metadata["study-plan"],
                    CONFIG_FILE,
                    heading_required=False,
                    remove_title=False,
                ).html_string
            pikau_course_assessment_description = pikau_course_metadata.get("assessment-description", "")
            if pikau_course_assessment_description:
                pikau_course_assessment_description = self.convert_md_file(
                    pikau_course_metadata["assessment-description"],
                    CONFIG_FILE,
                    heading_required=False,
                    remove_title=False,
                ).html_string
            pikau_course_assessment_items = pikau_course_metadata.get("assessment-items", "")
            if pikau_course_assessment_items:
                pikau_course_assessment_items = self.convert_md_file(
                    pikau_course_metadata["assessment-items"],
                    CONFIG_FILE,
                    heading_required=False,
                    remove_title=False,
                ).html_string

            cover_photo = pikau_course_metadata.get("cover-photo", COVER_PHOTO_DEFAULT)
            trailer_video = pikau_course_metadata.get("trailer-video", "")

            defaults = {
                "name": pikau_course_metadata["name"],
                "status": pikau_course_metadata["status"],
                "language": pikau_course_metadata["language"],
                "topic": Topic.objects.get(slug=pikau_course_metadata["topic"]),
                "level": Level.objects.get(slug=pikau_course_metadata["level"]),
                "trailer_video": trailer_video,
                "cover_photo": cover_photo,
                "overview": pikau_course_overview,
                "readiness_level": pikau_course_metadata.get("readiness-level"),
                "study_plan": pikau_course_study_plan,
                "assessment_description": pikau_course_assessment_description,
                "assessment_items": pikau_course_assessment_items,
            }

            pikau_course, created = PikauCourse.objects.update_or_create(
                slug=pikau_course_slug,
                defaults=defaults,
            )

            # If no project item, create one
            if not hasattr(pikau_course, "project_item") or pikau_course.project_item is None:
                project_item = ProjectItem.objects.create(
                    name=pikau_course.name,
                    pikau_course=pikau_course,
                    item_type=ProjectItem.ITEM_TYPE_PIKAU,
                )
                pikau_course.project_item = project_item
                pikau_course.save()

            for pikau_course_tag_slug in pikau_course_metadata.get("tags", list()):
                pikau_course.tags.add(Tag.objects.get(slug=pikau_course_tag_slug))

            for pikau_course_progress_outcome_slug in pikau_course_metadata.get("progress-outcomes", list()):
                outcome = ProgressOutcome.objects.get(slug=pikau_course_progress_outcome_slug)
                pikau_course.progress_outcomes.add(outcome)

            for pikau_course_glossary_term_slug in pikau_course_metadata.get("glossary", list()):
                pikau_course.glossary_terms.add(GlossaryTerm.objects.get(slug=pikau_course_glossary_term_slug))

            for pikau_course_prerequisite_slug in pikau_course_metadata.get("prerequisites", list()):
                pikau_course.prerequisites.add(PikauCourse.objects.get(slug=pikau_course_prerequisite_slug))

            # Check cover photo, trailer video, and extra files are logged
            pikau_course.project_item.files.add(find_file(filename=cover_photo))
            if trailer_video:
                pikau_course.project_item.files.add(find_file(filename=trailer_video))
            for file_slug in pikau_course_metadata.get("extra-files", list()):
                pikau_course.project_item.files.add(find_file(slug=file_slug))

            # Delete all existing units for course
            # since the will be loaded from raw data.
            PikauUnit.objects.filter(pikau_course=pikau_course).delete()

            pikau_course_number = 1
            for module_data in pikau_course_metadata["content"]:
                module_slug = module_data["slug"]
                module_name = module_data["module"]
                for unit_slug in module_data["units"]:
                    unit_content = self.convert_md_file(
                        os.path.join(module_slug, unit_slug) + ".md",
                        CONFIG_FILE,
                        heading_required=True,
                        remove_title=True,
                    )
                    # Check files in content
                    for filename in unit_content.required_files["images"]:
                        pikau_course.project_item.files.add(find_file(filename=filename))

                    pikau_course.content.create(
                        slug=unit_slug,
                        pikau_course=pikau_course,
                        name=unit_content.title,
                        content=unit_content.html_string,
                        module_name=module_name,
                        number=pikau_course_number,
                    )
                    pikau_course_number += 1

            # Add attributions page
            if pikau_course.project_item.files.exists():
                pikau_course_files = pikau_course.project_item.files.order_by("title")
                html = "<ul>"
                for pikau_course_file in pikau_course_files:
                    html += "<li>{}</li>".format(pikau_course_file.attribution(html=True))
                html += "</ul>"
                pikau_course.content.create(
                    slug="attributions",
                    pikau_course=pikau_course,
                    name="Attributions",
                    content=html,
                    module_name=module_name,
                    number=pikau_course_number,
                )
                pikau_course_number += 1
            self.log_object_creation(created, pikau_course)

        pikau_courses_with_postreqs = PikauCourse.objects.filter(postrequisites__isnull=False).distinct()
        for pikau_course in pikau_courses_with_postreqs:
            try:
                wrapping_up_unit = PikauUnit.objects.get(
                    pikau_course=pikau_course,
                    slug="wrapping-up"
                )
            except ObjectDoesNotExist:
                wrapping_up_unit = None
            if wrapping_up_unit:
                html = wrapping_up_unit.content
                html += "<p>You might like to continue your journey with these pīkau:</p>"
                html += "<ul>"
                for postrequisite in pikau_course.postrequisites.order_by("name"):
                    html += "<li><a href='{href}'>{text}</a></li>".format(
                        href=postrequisite.get_absolute_url(),
                        text=postrequisite.name,
                    )
                html += "</ul>"
                wrapping_up_unit.content = html
                wrapping_up_unit.save()

        self.log("All pikau courses loaded!\n")
