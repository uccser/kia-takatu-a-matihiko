from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class PikauCourseViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_pikau_course_list_view_with_no_courses(self):
        url = reverse("pikau:pikau_course_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["pikau_courses"]), 0)

    def test_pikau_course_list_view_with_one_course(self):
        self.test_data.create_pikau_course(1)

        url = reverse("pikau:pikau_course_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["pikau_courses"]), 1)
        self.assertQuerysetEqual(
            response.context["pikau_courses"],
            ["<PikauCourse: Pikau Course 1>"]
        )

    def test_pikau_course_list_view_with_two_courses(self):
        self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_course(2)

        url = reverse("pikau:pikau_course_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["pikau_courses"]), 2)
        self.assertQuerysetEqual(
            response.context["pikau_courses"],
            [
                "<PikauCourse: Pikau Course 1>",
                "<PikauCourse: Pikau Course 2>",
            ]
        )

    def test_pikau_course_view_with_valid_slug(self):
        self.test_data.create_pikau_course(1)

        url = reverse("pikau:pikau_course", kwargs={"slug": "pikau-course-1"})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(url, "/pikau/pikau-courses/pikau-course-1/")

    def test_pikau_course_view_with_invalid_slug(self):
        self.test_data.create_pikau_course(1)

        url = reverse("pikau:pikau_course", kwargs={"slug": "pikau-course-5"})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pikau_course_content_view_with_valid_slug(self):
        pikau_course_1 = self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_unit(pikau_course_1, 1)

        url = reverse("pikau:pikau_content", kwargs={"slug": "pikau-course-1"})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Pikau Course 1")

    def test_pikau_course_content_view_with_invalid_slug(self):
        pikau_course_1 = self.test_data.create_pikau_course(1)
        self.test_data.create_pikau_unit(pikau_course_1, 1)

        url = reverse("pikau:pikau_content", kwargs={"slug": "pikau-course-5"})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pikau_course_content_view_with_no_pikau_units(self):
        self.test_data.create_pikau_course(1)

        url = reverse("pikau:pikau_content", kwargs={"slug": "pikau-course-1"})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
