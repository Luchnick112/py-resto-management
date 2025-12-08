from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, DishType, Dish

COOK_URL = reverse("kitchen:cook-list")
DISH_URL = reverse("kitchen:dish-list")
DISH_TYPE_URL = reverse("kitchen:dish-type-list")


class PublicCookTests(TestCase):
    def test_login_required(self):
        res = self.client.get(COOK_URL)
        self.assertEqual(res.status_code, 302)
        self.assertIn("/login/", res.url)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_cooks(self):
        Cook.objects.create(username="cook1", password="pass123", years_of_experience=5)
        Cook.objects.create(username="cook2", password="pass123", years_of_experience=10)
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)
        cooks = Cook.objects.all().order_by("last_name")
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")


class PrivateDishTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(name="Dessert")

    def test_create_dish(self):
        form_data = {
            "name": "Cake",
            "description": "Chocolate cake",
            "price": 12.50,
            "dish_type": self.dish_type.id,
        }
        self.client.post(reverse("kitchen:dish-create"), data=form_data)
        new_dish = Dish.objects.get(name=form_data["name"])
        self.assertEqual(new_dish.description, form_data["description"])
        self.assertEqual(float(new_dish.price), form_data["price"])
        self.assertEqual(new_dish.dish_type, self.dish_type)


class DishSearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="search_user", password="pass123"
        )
        self.client.force_login(self.user)
        dish_type = DishType.objects.create(name="Main")
        Dish.objects.create(name="Pizza", description="Cheese", price=10, dish_type=dish_type)
        Dish.objects.create(name="Soup", description="Tomato", price=5, dish_type=dish_type)

    def test_search_dish_by_name(self):
        response = self.client.get(DISH_URL, {"name": "piz"})
        self.assertContains(response, "Pizza")
        self.assertNotContains(response, "Soup")


class DishTypeSearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="search_user", password="pass123"
        )
        self.client.force_login(self.user)
        DishType.objects.create(name="Starter")
        DishType.objects.create(name="Main")

    def test_search_dish_type_by_name(self):
        response = self.client.get(DISH_TYPE_URL, {"name": "start"})
        self.assertContains(response, "Starter")
        self.assertNotContains(response, "Main")
