from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator

from pikau.models import Level

from django.db import IntegrityError

class LevelModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()

    def test_level_model_one_level(self):
    	level = self.test_data.create_level(1)
    	query_result = Level.objects.get(slug="level-1")
    	self.assertEqual(query_result, level)

    def test_level_model_two_levels(self):
    	level_1 = self.test_data.create_level(1)
    	level_2 = self.test_data.create_level(2)
    	self.assertQuerysetEqual(
    		Level.objects.all(),
    		[
    		    "<Level: level-1-name>",
    		    "<Level: level-2-name>",
    		],
    		ordered=False
    	)

    def test_level_model_uniqueness(self):
        level = self.test_data.create_level(1)
        self.assertRaises(
            IntegrityError, 
            lambda: self.test_data.create_level(1)
        )

    def test_level_model_str(self):
        level = self.test_data.create_level(1)
        self.assertEqual(
            level.__str__(),
            "level-1-name"
        )
