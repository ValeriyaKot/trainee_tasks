from rest_framework import serializers
from .models import Cart
from apps.account.serializers import UserSerializer


class CartSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    # items = serializers.StringRelatedField(many=True)
    total_price = serializers.SerializerMethodField()
    number_of_items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.get_total_price()

    def get_number_of_items(self, obj):
        return obj.get_number_of_items()