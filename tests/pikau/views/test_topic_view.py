from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class TopicViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_pikau_topic_view_with_valid_slug(self):
        self.test_data.create_topic(1)

        url = reverse("pikau:topic", kwargs={"slug": "topic-1"})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(url, "/pikau/topics/view/topic-1/")

    def test_pikau_topic_view_with_invalid_slug(self):
        self.test_data.create_topic(1)

        url = reverse("pikau:topic", kwargs={"slug": "topic-5"})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pikau_topic_list_view_with_no_topics(self):
        url = reverse("pikau:topic_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["topics"]), 0)

    def test_pikau_topic_list_view_with_one_topic(self):
        self.test_data.create_topic(1)

        url = reverse("pikau:topic_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["topics"]), 1)
        self.assertQuerysetEqual(
            response.context["topics"],
            ["<Topic: topic-1-name>"]
        )

    def test_pikau_topic_list_view_with_two_topics(self):
        self.test_data.create_topic(1)
        self.test_data.create_topic(2)

        url = reverse("pikau:topic_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["topics"]), 2)
        self.assertQuerysetEqual(
            response.context["topics"],
            [
                "<Topic: topic-1-name>",
                "<Topic: topic-2-name>",
            ]
        )

    def test_pikau_topic_list_view_order(self):
        self.test_data.create_topic(3)
        self.test_data.create_topic(2)
        self.test_data.create_topic(1)

        url = reverse("pikau:topic_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["topics"]), 3)
        self.assertQuerysetEqual(
            response.context["topics"],
            [
                "<Topic: topic-1-name>",
                "<Topic: topic-2-name>",
                "<Topic: topic-3-name>",
            ]
        )
