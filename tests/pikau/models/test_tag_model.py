from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator

from pikau.models import Tag
from django.db import IntegrityError


class TagModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()

    def test_tag_model_one_tag(self):
        tag = self.test_data.create_tag(1)
        query_result = Tag.objects.get(slug="tag-1")
        self.assertEqual(query_result, tag)

    def test_tag_model_two_tags(self):
        self.test_data.create_tag(1)
        self.test_data.create_tag(2)
        self.assertQuerysetEqual(
            Tag.objects.all(),
            [
                "<Tag: tag-1-name>",
                "<Tag: tag-2-name>",
            ],
            ordered=False
        )

    def test_tag_model_uniqueness(self):
        self.test_data.create_tag(1)
        self.assertRaises(
            IntegrityError,
            lambda: self.test_data.create_tag(1)
        )

    def test_tag_model_str(self):
        tag = self.test_data.create_tag(1)
        self.assertEqual(
            tag.__str__(),
            "tag-1-name"
        )
