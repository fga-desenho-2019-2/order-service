from .models import Order, AddsItens
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class AddsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddsItens
        fields = '__all__'

    def save(self):
        addsItens = addsItens(
            adds_name = self.validated_data['adds_name'],
            adds_quantity = self.validated_data['adds_quantity'],
            adds_price = self.validated_data['adds_price'],
            adds_description = self.validated_data['adds_description'],
            adds_number_identification = self.validated_data['adds_number_identification']
        )

        return addsItens