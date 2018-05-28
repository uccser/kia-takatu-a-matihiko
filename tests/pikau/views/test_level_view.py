from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class LevelViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_pikau_level_view_with_no_levels(self):
        url = reverse("pikau:level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["levels"]), 0)

    def test_pikau_level_view_with_one_level(self):
        level = self.test_data.create_level(1)
        level.save()

        url = reverse("pikau:level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["levels"]), 1)
        self.assertQuerysetEqual(
            response.context["levels"],
            ["<Level: level-1-name>"]
        )

    def test_pikau_level_view_with_two_levels(self):
        level_1 = self.test_data.create_level(1)
        level_1.save()
        level_2 = self.test_data.create_level(2)
        level_2.save()

        url = reverse("pikau:level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["levels"]), 2)
        self.assertQuerysetEqual(
            response.context["levels"],
            [
                "<Level: level-1-name>",
                "<Level: level-2-name>",
            ]
        )

    def test_pikau_level_view_order(self):
        level_3 = self.test_data.create_level(3)
        level_3.save()
        level_2 = self.test_data.create_level(2)
        level_2.save()
        level_1 = self.test_data.create_level(1)
        level_1.save()

        url = reverse("pikau:level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["levels"]), 3)
        self.assertQuerysetEqual(
            response.context["levels"],
            [
                "<Level: level-1-name>",
                "<Level: level-2-name>",
                "<Level: level-3-name>"
            ]
        )