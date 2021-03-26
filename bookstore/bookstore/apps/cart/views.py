from rest_framework.permissions import IsAuthenticated
from .models import Cart
from rest_framework import viewsets
from .serializers import CartSerializer
from apps.book.models import Book
from rest_framework import status, generics
from rest_framework.response import Response
# from apps.order.models import Order
# from apps.order.serializer import OrderSerializer


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)



# class AddToCartView(generics.CreateAPIView):
#     serializer_class = CartSerializer
#
#     def post(self, request):
#         # book = Book.objects.get(pk=pk)
#         cart = Cart.objects.get(user=request.user)
#         # cart.items.add(book)
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             cart.items.add(request.data)
#
#             # serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)