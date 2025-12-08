from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse

from kitchen.validators import validate_years_of_experience


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(
        default=0,
        validators=[validate_years_of_experience],
        null=False,
        blank=False
    )

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", args=[str(self.id)])


    def __str__(self):
        return f"{self.username}: ({self.years_of_experience} years of experience)"


class DishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "dishes"
        verbose_name = "dish"

    def get_absolute_url(self):
        return reverse("kitchen:dish-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.name}, dish_type: {self.dish_type}, price: {self.price}"
