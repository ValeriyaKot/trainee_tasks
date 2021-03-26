from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from apps.cart.models import Cart
from apps.cart.serializers import CartSerializer
from rest_framework.response import Response




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['author', 'publishing_house', 'year']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ['country']