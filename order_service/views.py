from order_service.models import Order, OrderStatus, Item
from django.http import HttpResponse, JsonResponse
# from rest_framework import permissions, generics
from rest_framework.response import Response
from django.core import serializers
from rest_framework.decorators import action
# from rest_framework.generics import CreateAPIView
# from rest_framework.authtoken.models import Token
# from django.shortcuts import render
from .serializers import OrderSerializer, OrderStatusSerializer, ItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)

# class OrderList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer




@api_view(['GET'])
def list_user_orders(request, cpf):
    orders = Order.objects.filter(cpf_user = cpf)
    if not orders:
        return JsonResponse({"message": "Without user orders"}, status=HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)
    

@api_view(['GET'])
def list_all_orders(request):
    orders = Order.objects.all()
    if not orders:
        return JsonResponse({"message": "Without orders"}, status=HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def list_restaurant_orders(request, cnpj):
    orders = Order.objects.filter(cnpj_restaurant = cnpj)
    if not orders:
        return JsonResponse({"message": "Without restaurant orders"}, status=HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['PUT'])
def change_order_status(request):
    return Response("pedidos")


@api_view(['GET'])
def cancel_order(request):
    return Response("pedidos")


@api_view(['POST'])
def create_order(request):
    """
    Create an order with items
    """
    serializer = OrderSerializer(data = request.data)
    if serializer.is_valid():
        print(serializer)
        # serializer.save()
        return JsonResponse(serializer.data, status=HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_status(request):
    status = OrderStatus.objects.all()
    if not status:
        return JsonResponse({"message": "Status not exists"}, status=HTTP_404_NOT_FOUND)
    serializer = OrderStatusSerializer(status, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def list_items(request):
    items = Item.objects.all()
    if not items:
        return JsonResponse({"message": "Items not exists"}, status=HTTP_404_NOT_FOUND)
    serializer = OrderStatusSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)

# @api_view(['DELETE'])
# def delete_order(request, number_identification):

#     # If request is valid
#     order = Order.objects.get(pk=number_identification)
#     if (number_identification == None):
#         return Response({'error': 'Formulário inválido.'},
#                                 status=HTTP_400_BAD_REQUEST)
#     # If order exist
#     try:
#         order = Order.objects.get(pk=number_identification)
#     except:
#         return Response({'error': 'Produto não existe.'},
#                                 status=HTTP_404_NOT_FOUND)
#     order.delete()
#     return HttpResponse(status=204)


# @api_view(["POST"])
# def edit_order(request, number_identification):
#     order = Order.objects.get(pk=number_identification)
#     quantity = request.data.get('quantity')

#     if(number_identification == None):
#         return Response({'error':'Falha na requisição.'},status=HTTP_400_BAD_REQUEST)

#     try:
#         order = Order.objects.get(pk=number_identification)
#     except:
#         return Response({'error': 'Produto não existe.'},
#                                 status=HTTP_404_NOT_FOUND)
#     serializer = OrderSerializer(order, request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# class AddsList(generics.ListCreateAPIView):
#     queryset = Adds.objects.all()
#     serializer_class = AddsSerializer

# class AddsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Adds.objects.all()
#     serializer_class = AddsSerializer

# @api_view(['POST'])
# def create_adds(request):
#     serializer = AddsSerializer(data=request.data)
#     data = {}

#     if serializer.is_valid():
#         adds = serializer.save()
#         data['response'] = 'Adicional registrado com sucesso'

#     else:
#         data = serializer.errors

#     return Response(data)

# @api_view(["POST"])
# def list_adds(request):
#     adds = Adds.objects.all().values()
#     return Response(data=adds)

# @api_view(['DELETE'])
# def delete_adds(request, adds_number_identification):

#     # If request is valid
#     adds = Adds.objects.get(pk=adds_number_identification)
#     if (adds_number_identification == None):
#         return Response({'error': 'Formulário inválido.'},
#                                 status=HTTP_400_BAD_REQUEST)
#     # If adds exist
#     try:
#         adds = Adds.objects.get(pk=adds_number_identification)
#     except:
#         return Response({'error': 'Produto não existe.'},
#                                 status=HTTP_404_NOT_FOUND)
#     adds.delete()
#     return HttpResponse(status=204)


# @api_view(["POST"])
# def edit_adds(request, adds_number_identification):
#     adds = Adds.objects.get(pk=adds_number_identification)
#     quantity = request.data.get('quantity')

#     if(adds_number_identification == None):
#         return Response({'error':'Falha na requisição.'},status=HTTP_400_BAD_REQUEST)

#     try:
#         adds = Adds.objects.get(pk=adds_number_identification)
#     except:
#         return Response({'error': 'Produto não existe.'},
#                                 status=HTTP_404_NOT_FOUND)
#     serializer = AddsSerializer(adds, request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
