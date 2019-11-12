from .models import Order, Item
from rest_framework import serializers
from ..statics.status import ORDER_STATUS_DICT
from brutils import cpf, cnpj


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'value', 'observation', 'quantity']

    def validate_value(self, value):
        if (value > 0):
            return value
        raise serializers.ValidationError("Value must be positive!")

    
    def validate_quantity(self, value):
        if (value > 0):
            return value
        raise serializers.ValidationError("Quantity must be positive!")


    def validate_observation(self, value):
        if (len(value) < 200):
            return value
        raise serializers.ValidationError("Observation must be less than 200 characters!")


class OrderSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'cod', 'value', 'cpf_user', 'cnpj_restaurant', 'items', 'status' ]
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(order=order, **item_data)
        return order


    def validate_cpf_user(self, value):
        if (cpf.validate(value)):
            return value
        raise serializers.ValidationError("Invalid CPF digits!")

    
    def validate_cnpj_restaurant(self, value):
        if (cnpj.validate(value)):
            return value
        raise serializers.ValidationError("Invalid CNPJ digits!")


    def validate_value(self, value):
        if (value > 0):
            return value
        raise serializers.ValidationError("Value must be positive!")