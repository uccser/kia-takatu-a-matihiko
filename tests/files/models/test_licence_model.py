from tests.BaseTestWithDB import BaseTestWithDB
from tests.files.FileTestDataGenerator import FileTestDataGenerator

from files.models import Licence
from django.db import IntegrityError

class LicenceModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = FileTestDataGenerator()

    def test_licence_str(self):
        obj = self.test_data.create_licence(1)
        self.assertEqual(
            obj.__str__(),
            "Licence 1"
        )

    def test_licence_model_one_licence(self):
        licence = self.test_data.create_licence(1)
        query_result = Licence.objects.get(name="Licence 1")
        self.assertEqual(query_result, licence)

    def test_licence_model_two_licences(self):
        licence_1 = self.test_data.create_licence(1)
        licence_2 = self.test_data.create_licence(2)
        self.assertQuerysetEqual(
            Licence.objects.all(),
            [
                "<Licence: Licence 1>",
                "<Licence: Licence 2>",
            ],
            ordered=False
        )

    def test_licence_model_uniqueness(self):
        licence = self.test_data.create_licence(1)
        self.assertRaises(
            IntegrityError, 
            lambda: self.test_data.create_licence(1)
        )

    def test_licence_model_ordering(self):
        licence_3 = self.test_data.create_licence(3)
        licence_1 = self.test_data.create_licence(1)
        licence_2 = self.test_data.create_licence(2)
        self.assertQuerysetEqual(
            Licence.objects.all(),
            [
                "<Licence: Licence 1>",
                "<Licence: Licence 2>",
                "<Licence: Licence 3>",
            ],
        )