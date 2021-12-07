from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class Snack(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="ibrahim", email="ibrahim@ibrahim.com", password="pass"
        )

        self.snack = Snack.objects.create(
            name="Butterfinger", rating=1, reviewer=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Butterfinger")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.name}", "Butterfinger")
        self.assertEqual(f"{self.snack.purchaser}","ibrahim")
        self.assertEqual(self.snack.description,'yummy2')

    # def test_thing_list_view(self):
    #     response = self.client.get(reverse("thing_list"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "pickle")
    #     self.assertTemplateUsed(response, "thing_list.html")

    # def test_thing_detail_view(self):
    #     response = self.client.get(reverse("thing_detail", args="1"))
    #     # no_response = self.client.get("/100000/")
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, "Reviewer: tester")
    #     self.assertTemplateUsed(response, "thing_detail.html")

    # def test_thing_create_view(self):
    #     response = self.client.post(
    #         reverse("thing_create"),
    #         {
    #             "name": "Rake",
    #             "rating": "2",
    #             "reviewer": self.user.id,
    #         }, follow=True
    #     )

    #     self.assertRedirects(response, reverse("thing_detail", args="2"))
    #     self.assertContains(response, "Details about Rake")

    # def test_thing_update_view_redirect(self):
    #     response = self.client.post(
    #         reverse("thing_update", args="1"),
    #         {"name": "Updated name","rating":"3","reviewer":self.user.id}
    #     )

    #     self.assertRedirects(response, reverse("thing_detail", args="1"))

    # def test_thing_delete_view(self):
    #     response = self.client.get(reverse("thing_delete", args="1"))
    #     self.assertEqual(response.status_code, 200)