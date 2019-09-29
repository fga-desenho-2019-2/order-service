from order_service.models import Order
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .serializers import OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        order = serializer.save()
        data['response'] = 'Pedido registrado com sucesso'
        data['name'] = order.name
        data['description'] = order.description
        data['quantity'] = order.quantity
        data['number_identification'] = order.number_identification

    else:
        data = serializer.errors

    return Response(data)

@api_view(["POST"])
def list_orders(request):
    orders = Order.objects.all().values()
    return Response(data=orders) 