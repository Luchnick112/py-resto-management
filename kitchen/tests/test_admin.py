from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class CookAdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test123"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook1",
            password="test456",
            years_of_experience=7,
        )

    def test_cook_years_of_experience_listed(self):
        """
        test that years_of_experience is in list_display on cook admin page
        """
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_years_of_experience_detail_listed(self):
        """
        test that years_of_experience is on cook detail admin page
        """
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)
