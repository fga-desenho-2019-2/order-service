from .models import OrderStatus, Order, Item
from rest_framework import serializers

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'value']


class OrderSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True, read_only=True )
    status = OrderStatusSerializer(many=False)

    class Meta:
        model = Order
        fields = ['value', 'cpf_user', 'cnpj_restaurant', 'items', 'status', 'cod']