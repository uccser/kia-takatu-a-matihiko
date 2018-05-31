from tests.BaseTestWithDB import BaseTestWithDB
from tests.files.FileTestDataGenerator import FileTestDataGenerator

from files.models import File
from django.db import IntegrityError

class FileModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = FileTestDataGenerator()

    def test_file_str(self):
        obj = self.test_data.create_file(1)
        self.assertEqual(
            obj.__str__(),
            "File 1"
        )
    def test_file_repr(self):
        obj = self.test_data.create_file(1)
        self.assertEqual(
            obj.__repr__(),
            "File: {}".format(obj.slug)
        )

    def test_file_model_one_file(self):
        file = self.test_data.create_file(1)
        query_result = File.objects.get(slug="file-1")
        self.assertEqual(query_result, file)

    def test_file_model_two_files(self):
        file_1 = self.test_data.create_file(1)
        file_2 = self.test_data.create_file(2)
        self.assertQuerysetEqual(
            File.objects.all(),
            [
                "File: file-1",
                "File: file-2"
            ],
            ordered=False
        )

    def test_file_model_uniqueness(self):
        file = self.test_data.create_file(1)
        self.assertRaises(
            IntegrityError, 
            lambda: self.test_data.create_file(1)
        )
