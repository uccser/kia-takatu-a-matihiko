from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class DocumentationViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_documentation_view(self):
        response = self.client.get(reverse("pikau:docs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertContains(response, "Pīkau Documentation")
