from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'order', views.OrderView)
# router.register(r'order_book', views.OrderBookView)



urlpatterns = [
    path('', include(router.urls)),
    path('add_to_order', views.AddToOrderView.as_view())
    # path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    # path('add_cart/', views.add_to_cart, name='add_cart'),
    # path('cart_item/<int:pk>/', views.CartDetailAPIView.as_view(), name='cart_item')
    # path('add_to_cart', views.add_to_cart)
]
