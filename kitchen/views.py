from django.http import HttpRequest
from django.shortcuts import render
from django.views import generic

from kitchen.models import Cook, DishType, Dish


def index(request: HttpRequest):
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
    }
    return render(request, "kitchen/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    queryset = Cook.objects.all().order_by("last_name")
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all().order_by("name")
    paginate_by = 5
    context_object_name = "dish_list"


class DishDetailView(generic.DetailView):
    model = Dish


class DishTypeListView(generic.ListView):
    model = DishType
    queryset = DishType.objects.all().order_by("name")
    paginate_by = 5
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"

