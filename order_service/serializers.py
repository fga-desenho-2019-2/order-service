from .models import Order, Adds, Item
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class AddsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adds
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'