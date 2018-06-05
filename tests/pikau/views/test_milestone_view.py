from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse
from django.template import defaultfilters

import datetime as dt
from datetime import datetime


class MilestoneViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()
        self.current_time = datetime.now()

    def test_pikau_milestone_list_view_with_no_milestones(self):
        url = reverse("pikau:milestone_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["milestones"]), 0)

    def test_pikau_milestone_list_view_with_one_milestone(self):
        self.test_data.create_milestone(1, self.current_time)

        url = reverse("pikau:milestone_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["milestones"]), 1)
        self.assertQuerysetEqual(
            response.context["milestones"],
            ["<Milestone: milestone-1 - {}>".format(defaultfilters.date(self.current_time))]
        )

    def test_pikau_milestone_list_view_order(self):
        date_1 = self.current_time
        date_2 = self.current_time + dt.timedelta(days=30)
        self.test_data.create_milestone(1, date_2)
        self.test_data.create_milestone(2, date_1)

        url = reverse("pikau:milestone_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual(
            response.context["milestones"],
            [
                "<Milestone: milestone-2 - {}>".format(defaultfilters.date(date_1)),
                "<Milestone: milestone-1 - {}>".format(defaultfilters.date(date_2)),
            ],
        )

    def test_pikau_milestone_list_view_with_two_milestones(self):
        self.test_data.create_milestone(1, self.current_time)

        url = reverse("pikau:milestone_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["milestones"]), 1)
        self.assertQuerysetEqual(
            response.context["milestones"],
            ["<Milestone: milestone-1 - {}>".format(defaultfilters.date(self.current_time))]
        )

    def test_pikau_milestone_list_view_milestone_status_course_count(self):
        # checks how many courses are on a certain status for a certain milestone
        pikau_course = self.test_data.create_pikau_course(1)
        milestone = self.test_data.create_milestone(1, self.current_time)
        pikau_course.milestone = milestone
        pikau_course.status = 3
        pikau_course.save()

        url = reverse("pikau:milestone_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        milestones = response.context["milestones"]
        milestone_1 = milestones[0]
        milestone_1_status_3_course_count = milestone_1.status[3]
        milestone_1_status_7_course_count = milestone_1.status[7]
        self.assertEqual(milestone_1_status_3_course_count, 1)
        self.assertEqual(milestone_1_status_7_course_count, 0)

    def test_pikau_milestone_list_view_status_stages(self):
        url = reverse("pikau:milestone_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        status_stages = [
            (1, 'Stage 1', 'Conceptualising'),
            (2, 'Stage 2', 'Developing'),
            (3, 'Stage 3', 'Reviewing\nAcademic'),
            (4, 'Stage 4', 'Reviewing\nLanguage'),
            (5, 'Stage 5', 'Reviewing\nTechnical'),
            (6, 'Stage 6', 'Completed'),
            (7, 'Stage 7', 'Completed\nPublished to iQualify'),
        ]
        self.assertEqual(response.context["status_stages"], status_stages)

    def test_milestone_view_no_milestones(self):
        url = reverse("pikau:milestone", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_milestone_view_with_valid_pk(self):
        self.test_data.create_milestone(1, self.current_time)
        url = reverse("pikau:milestone", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            url,
            "/pikau/milestones/1/"
        )

    def test_milestone_view_with_invalid_pk(self):
        self.test_data.create_milestone(1, self.current_time)
        url = reverse("pikau:milestone", kwargs={"pk": 5})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
