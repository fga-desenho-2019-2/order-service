from django.urls import path
from .views import (
    create_order, 
    update_status_order,
    list_user_orders, 
    list_restaurant_orders,
)

urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('list_user_orders/<str:cpf>', list_user_orders, name='list_user_orders'),
    path('list_restaurant_orders/<str:cnpj>', list_restaurant_orders, name='list_restaurant_orders'),
    path('update_status_order/<int:id_order>/<int:id_status>', update_status_order, name='update_status_order')
]
