from .models import Order, Item
from rest_framework import serializers
from .statics.status import ORDER_STATUS_DICT


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'value', 'observation', 'quantity']


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