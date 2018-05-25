from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator

from pikau.models import PikauUnit

from django.db import IntegrityError

class PikauUnitModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()

    def test_pikau_unit_model_one_unit(self):
        pikau_course = self.test_data.create_pikau_course("1")
        pikau_unit = self.test_data.create_pikau_unit(pikau_course, 1)
        query_result = PikauUnit.objects.get(slug="pikau-unit-1")
        self.assertEqual(query_result, pikau_unit)

    def test_pikau_unit_model_two_units_with_module_name(self):
        pikau_course = self.test_data.create_pikau_course("1")
        pikau_unit_1 = self.test_data.create_pikau_unit(pikau_course, 1, True)
        pikau_unit_2 = self.test_data.create_pikau_unit(pikau_course, 2, True)
        self.assertQuerysetEqual(
            PikauUnit.objects.all(),
            [
                "<PikauUnit: Pikau Course 1: pikau-unit-1-module-name - pikau-unit-1-name>",
                "<PikauUnit: Pikau Course 1: pikau-unit-2-module-name - pikau-unit-2-name>"
            ],
            ordered=False
        )

    def test_pikau_unit_model_two_units_without_module_name(self):
        pikau_course = self.test_data.create_pikau_course("1")
        pikau_unit_1 = self.test_data.create_pikau_unit(pikau_course, 1)
        pikau_unit_2 = self.test_data.create_pikau_unit(pikau_course, 2)
        self.assertQuerysetEqual(
            PikauUnit.objects.all(),
            [
                "<PikauUnit: Pikau Course 1: pikau-unit-1-name>",
                "<PikauUnit: Pikau Course 1: pikau-unit-2-name>"
            ],
            ordered=False
        )

    def test_pikau_unit_model_uniqueness(self):
        pikau_course = self.test_data.create_pikau_course("1")
        pikau_unit = self.test_data.create_pikau_unit(pikau_course, 1)
        self.assertRaises(
            IntegrityError, 
            lambda: self.test_data.create_pikau_unit(pikau_course, 1)
        )

    def test_pikau_unit_model_str_with_module(self):
        pikau_course = self.test_data.create_pikau_course("1")
        pikau_unit = self.test_data.create_pikau_unit(pikau_course, 1, True)
        self.assertEqual(
            pikau_unit.__str__(),
            "Pikau Course 1: pikau-unit-1-module-name - pikau-unit-1-name"
        )

    def test_pikau_unit_model_str_without_module(self):
        pikau_course = self.test_data.create_pikau_course("1")
        pikau_unit = self.test_data.create_pikau_unit(pikau_course, 1)
        self.assertEqual(
            pikau_unit.__str__(),
            "Pikau Course 1: pikau-unit-1-name"
        )

    def test_pikau_unit_model_ordering(self):
        pikau_course = self.test_data.create_pikau_course("1")
        pikau_unit_1 = self.test_data.create_pikau_unit(pikau_course, 1)
        pikau_unit_2 = self.test_data.create_pikau_unit(pikau_course, 2)
        pikau_unit_3 = self.test_data.create_pikau_unit(pikau_course, 3)
        self.assertQuerysetEqual(
            PikauUnit.objects.all(),
            [
                "<PikauUnit: Pikau Course 1: pikau-unit-1-name>",
                "<PikauUnit: Pikau Course 1: pikau-unit-2-name>",
                "<PikauUnit: Pikau Course 1: pikau-unit-3-name>"
            ]
        )
