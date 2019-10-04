from .models import Order, Adds
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class AddsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adds
        fields = '__all__'