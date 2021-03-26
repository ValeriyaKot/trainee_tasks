from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include


router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)


urlpatterns = [
	path('', include(router.urls)),
]