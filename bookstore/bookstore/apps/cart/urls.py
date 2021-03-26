from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'cart', views.CartView, basename='cart')


urlpatterns = [
    path('', include(router.urls)),
    # path('add_to_cart/', views.AddToCartView.as_view())
]
