from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator

from pikau.models import GlossaryTerm

from django.db import IntegrityError

class GlossaryModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()

    def test_glossary_model_one_glossary_term(self):
        glossary_term = self.test_data.create_glossary_term(1)
        query_result = GlossaryTerm.objects.get(slug="glossary-term-1")
        self.assertEqual(query_result, glossary_term)

    def test_glossary_model_two_glossary_terms(self):
        glossary_term_1 = self.test_data.create_glossary_term(1)
        glossary_term_2 = self.test_data.create_glossary_term(2)
        self.assertQuerysetEqual(
            GlossaryTerm.objects.all(),
            [
                "<GlossaryTerm: Glossary Term 1>",
                "<GlossaryTerm: Glossary Term 2>"
            ],
            ordered=False
        )

    def test_glossary_model_uniqueness(self):
        gloasary_term = self.test_data.create_glossary_term(1)
        self.assertRaises(
            IntegrityError, 
            lambda: self.test_data.create_glossary_term(1)
        )

    def test_glossary_model_str(self):
        glossary_term = self.test_data.create_glossary_term(1)
        self.assertEqual(
            glossary_term.__str__(),
            "Glossary Term 1"
        )
