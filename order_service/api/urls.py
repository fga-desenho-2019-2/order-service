from django.urls import path
from .views import (
    create_order, 
    update_status_order,
    list_user_orders, 
    list_restaurant_orders,
    update_avaliation_order
)

urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('list_user_orders/<str:cpf>/<int:status>', list_user_orders, name='list_user_orders'),
    path('list_restaurant_orders/<str:cnpj>/<int:status>', list_restaurant_orders, name='list_restaurant_orders'),
    path('update_status_order/<int:id_order>/<int:id_status>', update_status_order, name='update_status_order'),
    path('update_avaliation_order/<int:id_order>', update_avaliation_order, name='update_avaliation_order')
]
