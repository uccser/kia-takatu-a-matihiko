from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator

from pikau.models import ProgressOutcome
from django.db import IntegrityError


class ProgressOutcomeModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()

    def test_progress_outcome_model_one_progress_outcome(self):
    	progress_outcome = self.test_data.create_progress_outcome(1)
    	query_result = ProgressOutcome.objects.get(slug="progress-outcome-1")
    	self.assertEqual(query_result, progress_outcome)

    def test_progress_outcome_model_two_progress_outcomes(self):
        progress_outcome_1 = self.test_data.create_progress_outcome(1)
        progress_outcome_2 = self.test_data.create_progress_outcome(2)
        self.assertQuerysetEqual(
            ProgressOutcome.objects.all(),
            [
                "<ProgressOutcome: progress-outcome-1-name>",
                "<ProgressOutcome: progress-outcome-2-name>",
            ],
            ordered=False
        )

    def test_progress_outcome_model_uniqueness(self):
        progress_outcome = self.test_data.create_progress_outcome(1)
        self.assertRaises(
            IntegrityError, 
            lambda: self.test_data.create_progress_outcome(1), 
        )

    def test_progress_outcome_model_str(self):
        progress_outcome = self.test_data.create_progress_outcome(1)
        self.assertEqual(
            progress_outcome.__str__(),
            "progress-outcome-1-name"
        )

    # SQLite does not enforce max_length. This test may be used in the future
    # to validate max_length.
    #
    # def test_progress_outcome_model_abbreviation_max_length(self):
    #     abbreviation = "a" * 11 # max length for abbreviation is 10.
    #     self.assertRaises(
    #         IntegrityError,
    #         lambda: ProgressOutcome(
    #             slug="progress-outcome-1",
    #             name="progress-outcome-1-name",
    #             abbreviation=abbreviation,
    #             description="Description for progress outcome 1.",
    #             exemplars="progress-outcome-1",
    #         ),
    #     )
        

        
