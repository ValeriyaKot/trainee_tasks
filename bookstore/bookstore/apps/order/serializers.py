from rest_framework import serializers
from .models import Order
from apps.account.serializers import UserSerializer
from apps.book.serializers import BookSerializer




# class OrderBookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderBook
#         fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    # items = BookSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    number_of_items = serializers.SerializerMethodField()

    # items = BookSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.get_total_price()

    def get_number_of_items(self, obj):
        return obj.get_number_of_items()
