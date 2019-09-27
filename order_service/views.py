from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .serializers import OrderSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def order_serializer(request):
    serializer = OrderSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        order = serializer.save()
        data['response'] = 'Pedido registrado com sucesso'
        data['name'] = order.name
        data['description'] = order.description
        data['price'] = order.price
        data['quantity'] = order.quantity
        data['number_identification'] = order.number_identification

    else:
        data = serializer.errors

    return Response(data)