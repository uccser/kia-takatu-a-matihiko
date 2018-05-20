from http import HTTPStatus
from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from tests.files.FileTestDataGenerator import FileTestDataGenerator


class IndexViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = FileTestDataGenerator()

    def test_index_with_no_files(self):
        url = reverse("files:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_index_with_one_file(self):
        obj = self.test_data.create_file(1)
        url = reverse("files:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["file_list"],
            map(repr, [obj]),
        )

    def test_index_with_multiple_files(self):
        obj_1 = self.test_data.create_file(1)
        obj_3 = self.test_data.create_file(3)
        obj_2 = self.test_data.create_file(2)
        url = reverse("files:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["file_list"],
            map(repr, [obj_1, obj_2, obj_3]),
            ordered=False,
        )
