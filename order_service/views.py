from order_service.models import Order
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
def list_user_orders(request, cpf):
    """
    List all orders from a specific user
    """
    orders = Order.objects.filter(cpf_user = cpf)
    if not orders:
        return JsonResponse({"message": "Without user orders"}, status=HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)
    


@api_view(['GET'])
def list_restaurant_orders(request, cnpj):
    """
    List all orders from a specific restaurant
    """
    orders = Order.objects.filter(cnpj_restaurant = cnpj)
    if not orders:
        return JsonResponse({"message": "Without restaurant orders"}, status=HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['PUT'])
def change_order_status(request):
    """
    Edit an order status
    """
    return JsonResponse({ "msg": "Status changed"})



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

