from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator


class PikauCourseModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()

    def test_pikau_course_str(self):
        pikau_course = self.test_data.create_pikau_course(1)
        self.assertEqual(
            pikau_course.__str__(),
            "Pikau Course 1"
        )
