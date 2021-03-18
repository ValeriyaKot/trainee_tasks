from rest_framework import serializers
from account.serializers import UserSerializer
from .models import ToDoList


class ToDoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True, allow_null=True, required=False,
                                        style={'base_template': 'textarea.html'})
    available = serializers.BooleanField(required=False)
    user = UserSerializer(read_only=True)

    def create(self, validated_data):
        return ToDoList(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance
