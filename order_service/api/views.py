from order_service.api.models import Order
from django.http import JsonResponse
from .serializers import OrderSerializer, ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)


@api_view(['GET'])
def list_user_orders(request, cpf, status):
    """
    List orders from a specific user
    """
    if not status:
        orders = Order.objects.filter(cpf_user = cpf)
    else:
        orders = Order.objects.filter(cpf_user = cpf, status = status)

    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def list_restaurant_orders(request, cnpj, status):
    """
    List orders from a specific restaurant
    """
    if not status:
        orders = Order.objects.filter(cnpj_restaurant = cnpj)
    else: 
        orders = Order.objects.filter(cnpj_restaurant = cnpj, status = status)

    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['PUT'])
def update_status_order(request, id_order, id_status):
    """
    Edit an order status
    """
    order = Order.objects.filter(id = id_order)
    if not order:
        return JsonResponse({"message": "No order found"}, status=HTTP_404_NOT_FOUND)
    order.update(status=id_status)
    return JsonResponse({ "message": "Status changed" }, status=HTTP_200_OK)


@api_view(['PUT'])
def update_avaliation_order(request, id_order):
    """
    Edit an order avaliation
    """
    try:
        order = Order.objects.filter(id = id_order)
        if not order:
            return JsonResponse({"message": "No order found"}, status=HTTP_404_NOT_FOUND)
        desc = request.data["avaliation_description"]
        number = request.data["avaliation_number"]
        order.update(avaliation_description=desc, avaliation_number=number)
        return JsonResponse({ "message": "Avaliation changed" }, status=HTTP_200_OK)
    except:
        return JsonResponse({
            "avaliation_description": ["Este campo é obrigatório"],
            "avaliation_number": ["Este campo é obrigatório"],
        }, status=HTTP_400_BAD_REQUEST) 



@api_view(['POST'])
def create_order(request):
    """
    Create an order with items
    """
    serializer = OrderSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

