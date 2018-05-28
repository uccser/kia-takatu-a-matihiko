from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class TagViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_pikau_tag_view_with_valid_slug(self):
        tag = self.test_data.create_tag(1)
        tag.save()

        url = reverse("pikau:tag", kwargs={"slug": "tag-1"})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(url, "/pikau/tags/tag-1/")

    def test_pikau_tag_view_with_invalid_slug(self):
        tag = self.test_data.create_tag(1)
        tag.save()

        url = reverse("pikau:tag", kwargs={"slug": "tag-5"})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pikau_tag_list_view_with_no_tags(self):
        url = reverse("pikau:tag_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["tags"]), 0)

    def test_pikau_tag_list_view_with_one_tag(self):
        tag = self.test_data.create_tag(1)
        tag.save()

        url = reverse("pikau:tag_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["tags"]), 1)
        self.assertQuerysetEqual(
            response.context["tags"],
            ["<Tag: tag-1-name>"]
        )

    def test_pikau_tag_list_view_with_two_tags(self):
        tag_1 = self.test_data.create_tag(1)
        tag_1.save()
        tag_2 = self.test_data.create_tag(2)
        tag_2.save()

        url = reverse("pikau:tag_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["tags"]), 2)
        self.assertQuerysetEqual(
            response.context["tags"],
            [
                "<Tag: tag-1-name>",
                "<Tag: tag-2-name>",
            ]
        )

    def test_pikau_tag_list_view_order(self):
        tag_3 = self.test_data.create_tag(3)
        tag_3.save()
        tag_2 = self.test_data.create_tag(2)
        tag_2.save()
        tag_1 = self.test_data.create_tag(1)
        tag_1.save()

        url = reverse("pikau:tag_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["tags"]), 3)
        self.assertQuerysetEqual(
            response.context["tags"],
            [
                "<Tag: tag-1-name>",
                "<Tag: tag-2-name>",
                "<Tag: tag-3-name>"
            ]
        )