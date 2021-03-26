from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)

    class Meta:
        ordering = ('first_name', 'last_name', 'country',)


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    annotation = models.TextField(max_length=250, blank=True, null=True)
    publishing_house = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField(default=1)
    year = models.IntegerField(validators=[MaxValueValidator(datetime.now().year)])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('title', 'year', 'price', 'publishing_house',)
