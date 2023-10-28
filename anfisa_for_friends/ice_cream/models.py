from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from core.models import PublishedModel


# Категории
class Category(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        default=100,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(32767)
        ]
    )
    is_published = models.BooleanField(default=True)


# Топпинги
class Topping(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)


# Обёртки
class Wrapper(PublishedModel):
    title = models.CharField(max_length=256)


# Сорта мороженого
class IceCream(PublishedModel):
    is_on_main = models.BooleanField(default=False)
    title = models.CharField(max_length=256)
    description = models.TextField()
    # Создайте нужные связи между моделями:
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
        )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)