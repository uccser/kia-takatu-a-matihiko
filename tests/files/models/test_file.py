from tests.BaseTestWithDB import BaseTestWithDB
from tests.files.FileTestDataGenerator import FileTestDataGenerator


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
