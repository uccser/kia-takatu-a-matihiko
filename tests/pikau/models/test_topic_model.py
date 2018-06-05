from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator

from pikau.models import Topic
from django.db import IntegrityError


class TopicModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()

    def test_topic_model_one_topic(self):
        topic = self.test_data.create_topic(1)
        query_result = Topic.objects.get(slug="topic-1")
        self.assertEqual(query_result, topic)

    def test_topic_model_two_topics(self):
        self.test_data.create_topic(1)
        self.test_data.create_topic(2)
        self.assertQuerysetEqual(
            Topic.objects.all(),
            [
                "<Topic: topic-1-name>",
                "<Topic: topic-2-name>",
            ],
            ordered=False
        )

    def test_topic_model_uniqueness(self):
        self.test_data.create_topic(1)
        self.assertRaises(
            IntegrityError,
            lambda: self.test_data.create_topic(1)
        )

    def test_topic_model_str(self):
        tag = self.test_data.create_topic(1)
        self.assertEqual(
            tag.__str__(),
            "topic-1-name"
        )
