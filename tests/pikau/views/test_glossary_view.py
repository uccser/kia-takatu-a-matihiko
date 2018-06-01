from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class GlossaryViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_pikau_glossary_view_with_no_definitions(self):
        url = reverse("pikau:glossary")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["glossary_terms"]), 0)

    def test_pikau_glossary_view_with_one_definition(self):
        term = self.test_data.create_glossary_term(1)

        url = reverse("pikau:glossary")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["glossary_terms"]), 1)
        self.assertQuerysetEqual(
            response.context["glossary_terms"],
            ["<GlossaryTerm: Glossary Term 1>"]
        )

    def test_pikau_glossary_view_with_two_definitions(self):
        term_1 = self.test_data.create_glossary_term(1)
        term_2 = self.test_data.create_glossary_term(2)

        url = reverse("pikau:glossary")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["glossary_terms"]), 2)
        self.assertQuerysetEqual(
            response.context["glossary_terms"],
            [
                "<GlossaryTerm: Glossary Term 1>", 
                "<GlossaryTerm: Glossary Term 2>",
            ]
        )

    def test_pikau_glossary_view_order(self):
        term_3 = self.test_data.create_glossary_term(3)
        term_2 = self.test_data.create_glossary_term(2)
        term_1 = self.test_data.create_glossary_term(1)

        url = reverse("pikau:glossary")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["glossary_terms"]), 3)
        self.assertQuerysetEqual(
            response.context["glossary_terms"],
            [
                "<GlossaryTerm: Glossary Term 1>",
                "<GlossaryTerm: Glossary Term 2>",
                "<GlossaryTerm: Glossary Term 3>",
            ]
        )
