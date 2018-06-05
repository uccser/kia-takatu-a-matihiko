from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class ProgressOutcomeViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_pikau_progress_outcome_view_with_valid_slug(self):
        self.test_data.create_progress_outcome(1)

        kwargs = {
            "slug": "progress-outcome-1",
        }
        url = reverse("pikau:progress_outcome", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            url,
            "/pikau/progress-outcomes/progress-outcome-1/"
        )

    def test_pikau_progress_outcome_view_with_invalid_slug(self):
        self.test_data.create_progress_outcome(1)

        kwargs = {
            "slug": "progress-outcome-5",
        }
        url = reverse("pikau:progress_outcome", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    # TODO: Add tests for heatmap.
