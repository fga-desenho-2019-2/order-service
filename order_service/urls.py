# !Prioridade!
# Criar um novo pedido - OK
# Listar o pedido de um usuário - OK
# Listar os pedidos de um restaurante - OK
# Mudar o status de um pedido


from django.urls import path
from .views import (
    create_order, 
    list_user_orders, 
    list_restaurant_orders,
)

urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('list_user_orders/<str:cpf>', list_user_orders, name='list_user_orders'),
    path('list_restaurant_orders/<str:cnpj>', list_restaurant_orders, name='list_restaurant_orders'),
]
