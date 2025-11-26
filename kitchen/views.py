from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import render

from kitchen.models import Cook, DishType, Dish


def index(request: HttpRequest):
    num_cooks = get_user_model().objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
    }
    return render(request, "kitchen/index.html", context=context)
