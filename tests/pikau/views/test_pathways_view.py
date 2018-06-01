from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse

from pikau.models import READINESS_LEVELS

class PathwaysViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_pathways_view(self):
        response = self.client.get(reverse("pikau:pathways"))
        self.assertEqual(200, response.status_code)

    def test_pathways_view_context_readiness_levels(self):
        response = self.client.get(reverse("pikau:pathways"))
        self.assertEqual(200, response.status_code)   
        self.assertEqual(response.context["readiness_levels"], READINESS_LEVELS)

    # TODO: test pathways notation - utils test.