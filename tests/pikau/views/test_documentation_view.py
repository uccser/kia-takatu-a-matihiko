from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse
from http import HTTPStatus

from pikau.models import (
    Level,
    ProgressOutcome,
    Topic,
    Tag,
    STATUS_CHOICES,
    READINESS_LEVELS,
)


class DocumentationViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = PikauTestDataGenerator()
        self.language = "en"

    def test_documentation_view(self):
        response = self.client.get(reverse("pikau:docs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertContains(response, "Pīkau Documentation")

    def test_documentation_view_context_status_stages(self):
        response = self.client.get(reverse("pikau:docs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(response.context["status_stages"], STATUS_CHOICES)

    def test_documentation_view_context_topics(self):
        topic_1 = self.test_data.create_topic(1)
        topic_2 = self.test_data.create_topic(2)

        response = self.client.get(reverse("pikau:docs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["topics"], 
            [
                "<Topic: topic-1-name>",
                "<Topic: topic-2-name>",
            ]
        )

    def test_documentation_view_context_levels(self):
        level_1 = self.test_data.create_level(1)
        level_2 = self.test_data.create_level(2)

        response = self.client.get(reverse("pikau:docs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["levels"],
            [
                "<Level: level-1-name>",
                "<Level: level-2-name>",
            ]
        )

    def test_documentation_view_context_progress_outcomes(self):
        progress_outcome_1 = self.test_data.create_progress_outcome(1)
        progress_outcome_2 = self.test_data.create_progress_outcome(2)

        response = self.client.get(reverse("pikau:docs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            ProgressOutcome.objects.all(),
            [
                "<ProgressOutcome: progress-outcome-1-name>",
                "<ProgressOutcome: progress-outcome-2-name>",
            ],
            ordered=False
        )

    def test_documentation_view_context_srt_tags(self):
        tag_1 = Tag(
            slug="srt-tag-1",
            name="srt-tag-1-name",
            description="<p>Description for tag 1.</p>",
        )
        tag_1.save()

        tag_2 = Tag(
            slug="srt-tag-2",
            name="srt-tag-2-name",
            description="<p>Description for tag 2.</p>",
        )
        tag_2.save()

        response = self.client.get(reverse("pikau:docs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["srt_tags"],
            [
                "<Tag: srt-tag-1-name>",
                "<Tag: srt-tag-2-name>",
            ]
        )

    def test_documentation_view_context_readiness_levels(self):
        response = self.client.get(reverse("pikau:docs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(response.context["readiness_levels"], READINESS_LEVELS)

    def test_documentation_view_with_no_data(self):
        response = self.client.get(reverse("pikau:docs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(response.context["status_stages"], STATUS_CHOICES)
        self.assertQuerysetEqual(response.context["topics"], [])
        self.assertQuerysetEqual(response.context["levels"], [])
        self.assertQuerysetEqual(response.context["progress_outcomes"], [])
        self.assertEqual(response.context["readiness_levels"], READINESS_LEVELS)