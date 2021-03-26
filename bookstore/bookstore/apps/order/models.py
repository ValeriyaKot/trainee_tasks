from django.db import models
from django.contrib.auth.models import User
from apps.book.models import Book


ORDER_STATUS = [
    ('subbmited', 'Subbmited'),
    ('ready', 'Ready'),
    ('delivered', 'Delivered'),
]

# class OrderBook(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1, blank=True)
#
#     def get_item_price(self):
#         return self.quantity * self.book.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book)
    order_status = models.CharField(max_length=250, choices=ORDER_STATUS)

    def get_total_price(self):
        calc = [book.price for book in self.items.all()]
        return sum(calc)

    def get_number_of_items(self):
        return len(self.items.all())

