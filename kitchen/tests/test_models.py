from django.contrib.auth import get_user_model
from django.test import TestCase


from kitchen.models import Dish, DishType


class KitchenModelsTests(TestCase):
    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="cook1",
            password="test123",
            first_name="Test",
            last_name="Cook",
            years_of_experience=7,
        )
        self.assertEqual(
            str(cook),
            f"{cook.username}: ({cook.years_of_experience} years of experience)"
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Main Course")
        self.assertEqual(str(dish_type), "Main Course")

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Dessert")
        cook = get_user_model().objects.create_user(
            username="cook2",
            password="test123",
            years_of_experience=3,
        )
        dish = Dish.objects.create(
            name="Cheesecake",
            description="Delicious cake",
            price=9.99,
            dish_type=dish_type,
        )
        dish.cooks.add(cook)
        self.assertEqual(
            str(dish),
            f"{dish.name}, dish_type: {dish.dish_type}, price: {dish.price}"
        )

    def test_create_cook_with_years_of_experience(self):
        username = "cook3"
        password = "test123"
        years = 12
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years,
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years)
        self.assertTrue(cook.check_password(password))
