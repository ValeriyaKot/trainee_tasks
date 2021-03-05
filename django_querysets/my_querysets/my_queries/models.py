from django.db import models


class MyQuerySet(models.QuerySet):
    def create_object(self, **kwargs):
        return self.create(**kwargs)

    def create_five_objects(self, obj_list):
        return self.bulk_create(obj_list, batch_size=5)

    def update_object(self, **kwargs):
        return self.update(**kwargs)

    def delete_object(self, **kwargs):
        return self.filter(**kwargs).delete()

    def delete_first_objects(self, id_number):
        """Delete all objects to id number"""
        return self.filter(id__lte=id_number).delete()

    def delete_last_object(self):
        return self.order_by('id').last().delete()

    def is_published_true(self):
        return self.filter(is_published=True)

    def merge_objects(self, *args):
        return self.select_related(*args)

    def sort_by_title(self):
        return self.all().order_by('title')

    def count_topics(self):
        return self.select_related('category').count()

    def filter_by_category(self, name):
        return self.filter(category__name=name)


class NewsManager(models.Manager):
    def get_queryset(self):
        return MyQuerySet(self.model, using=self._db)

    def create_object(self, **kwargs):
        return self.get_queryset().create_object(**kwargs)

    def create_five_objects(self, obj_list):
        return self.get_queryset().create_five_objects(obj_list)

    def update_object(self, **kwargs):
        return self.get_queryset().update_object(**kwargs)

    def delete_object(self, **kwargs):
        return self.get_queryset().delete_object(**kwargs)

    def delete_first_objects(self, id_number):
        return self.get_queryset().delete_first_objects(id_number)

    def delete_last_object(self):
        return self.get_queryset().delete_last_object()

    def is_published_true(self):
        return self.get_queryset().is_published_true()

    def merge_objects(self, *args):
        return self.get_queryset().merge_objects(*args)

    def sort_by_title(self):
        return self.get_queryset().sort_by_title()

    def count_topics(self):
        return self.get_queryset().count_topics()

    def filter_by_category(self, name):
        return self.get_queryset().filter_by_category(name)
