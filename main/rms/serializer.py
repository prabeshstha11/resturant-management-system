from rest_framework import serializers
from .models import Category, Table, Food


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
    
class FoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    ## mapping category id to category object
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())   
    
    def create(self, validated_data):
        food = Food.objects.create(**validated_data)
        return food