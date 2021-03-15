from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.db.models import F


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


class StyleQuerySet(models.QuerySet):
    def delete_style(self, style_id):
        return self.filter(id=style_id).update(deleted=True, deleted_at=timezone.now())


class AuthorQuerySet(models.QuerySet):
    def delete_author(self, author_id):
        return self.filter(id=author_id).update(deleted=True, deleted_at=timezone.now())


class BookQuerySet(models.QuerySet):
    def delete_book(self, book_id):
        return self.filter(id=book_id).update(deleted=True, deleted_at=timezone.now())

    def sort_authors(self):
        return self.prefetch_related('authors').order_by('authors__name').values_list('authors__name', flat=True) \
            .distinct()

    def get_authors_by_country(self, country):
        return self.prefetch_related('authors').filter(authors__country=country,
                                                       authors__age__gt=30,
                                                       authors__deleted=False) \
            .values_list('authors__name', flat=True).distinct()

    def get_books(self, author_name):
        return self.prefetch_related('authors').filter(authors__name=author_name, authors__deleted=False)

    def get_books_by_language(self, author_name, language):
        return self.prefetch_related('authors').filter(language=language,
                                                       authors__name=author_name,
                                                       authors__deleted=False
                                                       )

    def count_books_by_author(self, author_name):
        return self.prefetch_related('authors').filter(authors__name=author_name).count()

    def count_books_by_author_and_date(self, author_name, books_date):
        return self.prefetch_related('authors').filter(authors__name=author_name, year__gt=books_date).count()

    def count_pages(self, author_name):
        return self.prefetch_related('authors').filter(authors__name=author_name).aggregate(Sum('pages_number'))

    def count_pages_by_style(self, author_name, style):
        return self.prefetch_related('authors').filter(authors__name=author_name,
                                                       style__name=style
                                                       ).aggregate(Sum('pages_number'))

    def sort_by_name(self, method):
        if method == 'asc':
            return self.all().order_by(F('name').asc())
        elif method == 'desc':
            return self.all().order_by(F('name').desc())

    def get_deleted_authors(self, letter):
        return self.prefetch_related('authors').exclude(authors__deleted=False) \
            .filter(authors__name__startswith=letter).values_list('authors__name', flat=True)

    def get_authors_younger_than(self, age):
        return self.prefetch_related('authors').filter(authors__age__lt=age).values_list('authors__name', flat=True)

    def check_old_authors(self):
        authors = self.prefetch_related('authors').filter(authors__age__gte=80).values_list('authors__name', flat=True)
        return True if len(authors) is not 0 else False

    def check_old_book(self):
        books = self.filter(pages_number__gte=200, year__gt=100)
        return True if len(books) is not 0 else False

    def get_last_deleted_book(self):
        return self.order_by('-deleted_at').first()

    def get_last_deleted_author(self):
        return self.prefetch_related('authors').filter(authors__age__gte=55).order_by('authors__deleted_at') \
            .values_list('authors__name', flat=True).first()

    def get_info(self, book_name):
        return self.prefetch_related('authors').select_related('style').filter(name=book_name) \
            .values('name', 'year', 'authors__name', 'pages_number', 'style__name', 'language')

    def get_styles(self):
        return self.select_related('style').values('style__name', 'name').distinct()
