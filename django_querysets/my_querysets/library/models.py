from django.db import models
from my_queries.models import BookQuerySet, AuthorQuerySet, StyleQuerySet

LANGUAGE = [
    ('RU', 'Russian'),
    ('EN', 'English'),
    ('FR', 'French'),
    ('GE', 'German'),
    ('SP', 'Spanish'),
    ('OT_LANG', 'Other language')
]


class Name(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        abstract = True


class Date(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, default=None, null=True)

    class Meta:
        abstract = True


class Style(Name, Date):
    objects = StyleQuerySet.as_manager()

    def __str__(self):
        return self.name


class Author(Name, Date):
    country = models.CharField(max_length=250)
    age = models.IntegerField()
    objects = AuthorQuerySet.as_manager()

    def __str__(self):
        return self.name


class Book(Name, Date):
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    year = models.DateField()
    authors = models.ManyToManyField(Author)
    pages_number = models.IntegerField()
    language = models.CharField(max_length=250, choices=LANGUAGE, default='OT_LANG')
    objects = BookQuerySet.as_manager()

    def __str__(self):
        return '{}'.format(self.name)
