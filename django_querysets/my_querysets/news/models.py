from django.db import models
from my_queries.models import MyQuerySet


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    text = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    news = MyQuerySet.as_manager()

    def __str__(self):
        return self.title
