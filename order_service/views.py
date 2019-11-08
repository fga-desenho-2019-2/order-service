from order_service.models import Order, Adds
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .serializers import OrderSerializer, AddsSerializer, ItemSerializer
from django.shortcuts import get_object_or_404
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
    data = JSONParser().parse(request)
    
    items_data = data.pop('items')

    serializer_order = OrderSerializer(data=data)
    serializer_item  = ItemSerializer(data=items_data)

    if serializer_order.is_valid():
        serializer_order.save()
        return JsonResponse(serializer_order.data, status=201, safe=False)
    else:
        return JsonResponse(serializer_order.errors, status=400, safe=False)
    
    if serializer_item.is_valid():
        serializer_item.save()
        return JsonResponse(serializer_item.data, status=201, safe=False)
    else:
        return JsonResponse(serializer_item.errors, status=400, safe=False)

@api_view(['POST'])
def create_item(request):
    data = JSONParser().parse(request)
    serializer = ItemSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201, safe=False)
    
    return JsonResponse(serializer.errors, status=400, safe=False)

@api_view(["GET"])
def list_orders(request):
    orders = Order.objects.all().values()
    return Response(data=orders)

@api_view(['DELETE'])
def delete_order(request, number_identification):

    # If request is valid
    order = Order.objects.get(pk=number_identification)
    if (number_identification == None):
        return Response({'error': 'Formulário inválido.'},
                                status=HTTP_400_BAD_REQUEST)
    # If order exist
    try:
        order = Order.objects.get(pk=number_identification)
    except:
        return Response({'error': 'Produto não existe.'},
                                status=HTTP_404_NOT_FOUND)
    order.delete()
    return HttpResponse(status=204)


@api_view(["POST"])
def edit_order(request, number_identification):
    order = Order.objects.get(pk=number_identification)
    quantity = request.data.get('quantity')

    if(number_identification == None):
        return Response({'error':'Falha na requisição.'},status=HTTP_400_BAD_REQUEST)

    try:
        order = Order.objects.get(pk=number_identification)
    except:
        return Response({'error': 'Produto não existe.'},
                                status=HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class AddsList(generics.ListCreateAPIView):
    queryset = Adds.objects.all()
    serializer_class = AddsSerializer

class AddsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adds.objects.all()
    serializer_class = AddsSerializer

@api_view(['POST'])
def create_adds(request):
    serializer = AddsSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        adds = serializer.save()
        data['response'] = 'Adicional registrado com sucesso'

    else:
        data = serializer.errors

    return Response(data)

@api_view(["POST"])
def list_adds(request):
    adds = Adds.objects.all().values()
    return Response(data=adds)

@api_view(['DELETE'])
def delete_adds(request, adds_number_identification):

    # If request is valid
    adds = Adds.objects.get(pk=adds_number_identification)
    if (adds_number_identification == None):
        return Response({'error': 'Formulário inválido.'},
                                status=HTTP_400_BAD_REQUEST)
    # If adds exist
    try:
        adds = Adds.objects.get(pk=adds_number_identification)
    except:
        return Response({'error': 'Produto não existe.'},
                                status=HTTP_404_NOT_FOUND)
    adds.delete()
    return HttpResponse(status=204)


@api_view(["POST"])
def edit_adds(request, adds_number_identification):
    adds = Adds.objects.get(pk=adds_number_identification)
    quantity = request.data.get('quantity')

    if(adds_number_identification == None):
        return Response({'error':'Falha na requisição.'},status=HTTP_400_BAD_REQUEST)

    try:
        adds = Adds.objects.get(pk=adds_number_identification)
    except:
        return Response({'error': 'Produto não existe.'},
                                status=HTTP_404_NOT_FOUND)
    serializer = AddsSerializer(adds, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)