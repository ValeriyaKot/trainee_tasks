from django.contrib import admin
from apps.book.models import Book
from apps.cart.models import Cart

admin.site.register(Book)
admin.site.register(Cart)
