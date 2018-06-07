from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class ReadinessLevelViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_readiness_level_list_view_with_no_courses(self):
        url = reverse("pikau:readiness_level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        readiness_levels = response.context["readiness_levels"]
        for level in range(1, 6):
            level_data = readiness_levels[level]
            num_of_courses_on_level = level_data["count"]
            self.assertEqual(num_of_courses_on_level, 0)

    def test_readiness_level_list_view_with_one_course_for_all_levels(self):
        # create 1 course under each readiness level
        for level in range(1, 6):
            pikau_course = self.test_data.create_pikau_course(level)
            pikau_course.readiness_level = level
            pikau_course.save()

            url = reverse("pikau:readiness_level_list")
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)

            readiness_levels = response.context["readiness_levels"]
            level_data = readiness_levels[level]
            num_of_courses_on_level = level_data["count"]
            self.assertEqual(num_of_courses_on_level, 1)

    def test_readiness_level_list_view_multiple_courses_one_level(self):
        pikau_course_1 = self.test_data.create_pikau_course(1)
        pikau_course_1.readiness_level = 4
        pikau_course_1.save()

        pikau_course_2 = self.test_data.create_pikau_course(2)
        pikau_course_2.readiness_level = 4
        pikau_course_2.save()

        pikau_course_3 = self.test_data.create_pikau_course(3)
        pikau_course_3.readiness_level = 4
        pikau_course_3.save()

        url = reverse("pikau:readiness_level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        readiness_levels = response.context["readiness_levels"]
        level_data = readiness_levels[4]
        num_of_courses_on_level = level_data["count"]
        self.assertEqual(num_of_courses_on_level, 3)

    def test_readiness_level_list_view_multiple_courses_multiple_levels(self):
        pikau_course_1 = self.test_data.create_pikau_course(1)
        pikau_course_1.readiness_level = 2
        pikau_course_1.save()

        pikau_course_2 = self.test_data.create_pikau_course(2)
        pikau_course_2.readiness_level = 5
        pikau_course_2.save()

        pikau_course_3 = self.test_data.create_pikau_course(3)
        pikau_course_3.readiness_level = 1
        pikau_course_3.save()

        pikau_course_4 = self.test_data.create_pikau_course(4)
        pikau_course_4.readiness_level = 1
        pikau_course_4.save()

        pikau_course_5 = self.test_data.create_pikau_course(5)
        pikau_course_5.readiness_level = 2
        pikau_course_5.save()

        url = reverse("pikau:readiness_level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        readiness_levels = response.context["readiness_levels"]
        level_1_data = readiness_levels[1]
        level_2_data = readiness_levels[2]
        level_5_data = readiness_levels[5]
        num_of_courses_on_level_1 = level_1_data["count"]
        num_of_courses_on_level_2 = level_2_data["count"]
        num_of_courses_on_level_5 = level_5_data["count"]

        self.assertEqual(num_of_courses_on_level_1, 2)
        self.assertEqual(num_of_courses_on_level_2, 2)
        self.assertEqual(num_of_courses_on_level_5, 1)

    def test_readiness_level_view_no_courses(self):
        url = reverse("pikau:readiness_level", kwargs={"level_number": 2})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        readiness_level = response.context["readiness_level"]
        pikau_courses = readiness_level["pikau_courses"]
        self.assertQuerysetEqual(pikau_courses, [])

    def test_readiness_level_view_one_course(self):
        pikau_course = self.test_data.create_pikau_course(1)
        pikau_course.readiness_level = 5
        pikau_course.save()

        url = reverse("pikau:readiness_level", kwargs={"level_number": 5})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        readiness_level = response.context["readiness_level"]
        pikau_courses = readiness_level["pikau_courses"]
        self.assertQuerysetEqual(
            pikau_courses,
            ["<PikauCourse: Pikau Course 1>"]
        )

    def test_readiness_level_view_two_courses(self):
        pikau_course_1 = self.test_data.create_pikau_course(1)
        pikau_course_1.readiness_level = 3
        pikau_course_1.save()

        pikau_course_2 = self.test_data.create_pikau_course(2)
        pikau_course_2.readiness_level = 3
        pikau_course_2.save()

        url = reverse("pikau:readiness_level", kwargs={"level_number": 3})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        readiness_level = response.context["readiness_level"]
        pikau_courses = readiness_level["pikau_courses"]
        self.assertQuerysetEqual(
            pikau_courses,
            [
                "<PikauCourse: Pikau Course 1>",
                "<PikauCourse: Pikau Course 2>",
            ],
            ordered=False
        )

    def test_readiness_level_view_three_courses(self):
        pikau_course_1 = self.test_data.create_pikau_course(1)
        pikau_course_1.readiness_level = 4
        pikau_course_1.save()

        pikau_course_2 = self.test_data.create_pikau_course(2)
        pikau_course_2.readiness_level = 4
        pikau_course_2.save()

        pikau_course_3 = self.test_data.create_pikau_course(3)
        pikau_course_3.readiness_level = 4
        pikau_course_3.save()

        url = reverse("pikau:readiness_level", kwargs={"level_number": 4})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        readiness_level = response.context["readiness_level"]
        pikau_courses = readiness_level["pikau_courses"]
        self.assertQuerysetEqual(
            pikau_courses,
            [
                "<PikauCourse: Pikau Course 1>",
                "<PikauCourse: Pikau Course 2>",
                "<PikauCourse: Pikau Course 3>",
            ],
            ordered=False
        )

    def test_readiness_level_view_with_invalid_level(self):
        url = reverse("pikau:readiness_level", kwargs={"level_number": 6})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
