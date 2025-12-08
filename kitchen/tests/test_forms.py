from django.test import TestCase

from kitchen.forms import CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_years_of_experience_is_valid(self):
        form_data = {
            "username": "new_cook",
            "password1": "cook12test",
            "password2": "cook12test",
            "first_name": "Test first",
            "last_name": "Test last",
            "email": "test@example.com",
            "years_of_experience": 5,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        cook = form.save(commit=False)
        self.assertEqual(cook.username, form_data["username"])
        self.assertEqual(cook.first_name, form_data["first_name"])
        self.assertEqual(cook.last_name, form_data["last_name"])
        self.assertEqual(cook.email, form_data["email"])
        self.assertEqual(cook.years_of_experience, form_data["years_of_experience"])
