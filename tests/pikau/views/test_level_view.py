from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class LevelViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_pikau_level_view_with_valid_slug(self):
        self.test_data.create_level(1)

        url = reverse("pikau:level", kwargs={"slug": "level-1"})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(url, "/pikau/levels/level-1/")

    def test_pikau_level_view_with_invalid_slug(self):
        self.test_data.create_level(1)

        url = reverse("pikau:level", kwargs={"slug": "level-5"})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pikau_level_list_view_with_no_levels(self):
        url = reverse("pikau:level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["levels"]), 0)

    def test_pikau_level_list_view_with_one_level(self):
        self.test_data.create_level(1)

        url = reverse("pikau:level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["levels"]), 1)
        self.assertQuerysetEqual(
            response.context["levels"],
            ["<Level: level-1-name>"]
        )

    def test_pikau_level_list_view_with_two_levels(self):
        self.test_data.create_level(1)
        self.test_data.create_level(2)

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

    def test_pikau_level_list_view_order(self):
        self.test_data.create_level(3)
        self.test_data.create_level(2)
        self.test_data.create_level(1)

        url = reverse("pikau:level_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["levels"]), 3)
        self.assertQuerysetEqual(
            response.context["levels"],
            [
                "<Level: level-1-name>",
                "<Level: level-2-name>",
                "<Level: level-3-name>",
            ]
        )
