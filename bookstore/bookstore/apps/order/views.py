from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import  OrderSerializer
from .models import Order
from rest_framework import viewsets
from django.http import Http404
from apps.cart.models import Cart
from rest_framework.views import APIView
from .serializers import OrderSerializer


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

# class AddToOrderView(APIView):
#
#     def get(self, request):
#         cart = Cart.objects.get(user=request.user)
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(items=cart.items, user=request.user)
#         return Response(serializer.data)
