from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'account'
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profiles/', views.ProfileListCreateView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile'),
]
