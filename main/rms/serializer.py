from rest_framework import serializers
from .models import Category, Table


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get("name"))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    number = serializers.CharField()
    capacity = serializers.IntegerField()
    is_available = serializers.BooleanField()
    
    
    def create(self, validated_data):
        table = Table.objects.create(
            number=validated_data.get("number"),
            capacity=validated_data.get("capacity"),
            is_available=validated_data.get("is_available")
        )
        return table