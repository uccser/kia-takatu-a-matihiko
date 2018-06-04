from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class PikauUnitViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_pikau_unit_view_with_valid_slug(self):
        pikau_course = self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_unit(pikau_course, 1)

        kwargs = {
            "course_slug": "pikau-course-1",
            "unit_slug": "pikau-unit-1"
        }
        url = reverse("pikau:pikau_unit", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            url,
            "/pikau/pikau-courses/pikau-course-1/content/pikau-unit-1/"
        )

    def test_pikau_unit_view_with_invalid_unit_slug(self):
        pikau_course = self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_unit(pikau_course, 1)

        kwargs = {
            "course_slug": "pikau-course-1",
            "unit_slug": "pikau-unit-2"
        }
        url = reverse("pikau:pikau_unit", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pikau_unit_view_with_invalid_course_slug(self):
        pikau_course = self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_unit(pikau_course, 1)

        kwargs = {
            "course_slug": "pikau-course-2",
            "unit_slug": "pikau-unit-1"
        }
        url = reverse("pikau:pikau_unit", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pikau_unit_view_context_with_previous_unit(self):
        pikau_course = self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_unit(pikau_course, 1)
        self.test_data.create_pikau_unit(pikau_course, 2)

        kwargs = {
            "course_slug": "pikau-course-1",
            "unit_slug": "pikau-unit-2"
        }
        url = reverse("pikau:pikau_unit", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        previous_unit = response.context["previous_unit"]
        self.assertEqual(previous_unit, pikau_unit_1)

    def test_pikau_unit_view_context_with_next_unit(self):
        pikau_course = self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_unit(pikau_course, 1)
        self.test_data.create_pikau_unit(pikau_course, 2)

        kwargs = {
            "course_slug": "pikau-course-1",
            "unit_slug": "pikau-unit-1"
        }
        url = reverse("pikau:pikau_unit", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        next_unit = response.context["next_unit"]
        self.assertEqual(next_unit, pikau_unit_2)

    def test_pikau_unit_view_context_with_previous_and_next_unit(self):
        pikau_course = self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_unit(pikau_course, 1)
        self.test_data.create_pikau_unit(pikau_course, 2)
        self.test_data.create_pikau_unit(pikau_course, 3)

        kwargs = {
            "course_slug": "pikau-course-1",
            "unit_slug": "pikau-unit-2"
        }
        url = reverse("pikau:pikau_unit", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        previous_unit = response.context["previous_unit"]
        self.assertEqual(previous_unit, pikau_unit_1)
        next_unit = response.context["next_unit"]
        self.assertEqual(next_unit, pikau_unit_3)

    def test_pikau_unit_view_context_with_no_previous_or_next_units(self):
        pikau_course = self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_unit(pikau_course, 1)

        kwargs = {
            "course_slug": "pikau-course-1",
            "unit_slug": "pikau-unit-1"
        }
        url = reverse("pikau:pikau_unit", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        previous_unit = response.context["previous_unit"]
        self.assertEqual(previous_unit, None)
        next_unit = response.context["next_unit"]
        self.assertEqual(next_unit, None)
