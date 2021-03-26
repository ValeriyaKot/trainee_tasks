from django.db import models
from apps.book.models import Book
from django.contrib.auth.models import User



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    items = models.ManyToManyField(Book)

    def get_total_price(self):
        calc = [book.price for book in self.items.all()]
        return sum(calc)

    def get_number_of_items(self):
        return len(self.items.all())

