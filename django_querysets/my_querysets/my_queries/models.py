from django.db import models


class MyQuerySet(models.QuerySet):
    def create_five_objects(self, obj_list):
        return self.bulk_create(obj_list, batch_size=5)

    def delete_object(self, **kwargs):
        return self.filter(**kwargs).delete()

    def delete_first_objects(self, id_number):
        """Delete all objects to id number"""
        return self.filter(id__lte=id_number).delete()

    def delete_last_object(self):
        return self.order_by('id').last().delete()

    def is_published(self):
        return self.filter(is_published=True)

    def sort_by_title(self):
        return self.all().order_by('title')

    def count_topics(self):
        return self.select_related('category').count()

    def filter_by_category(self, name):
        return self.filter(category__name=name)
