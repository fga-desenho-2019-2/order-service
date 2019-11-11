# Endpoints necessários para serviço de pedidos

# !Prioridade!
# Criar um novo pedido
# Listar o pedido de um usuário
# Listar os pedidos de um restaurante
# Mudar o status de um pedido
# Cancelar um pedido


from django.urls import path
# from order_service import views
from .views import (
    create_order, 
    list_user_orders, 
    list_restaurant_orders,
    list_status,
    list_items,
    list_all_orders,
)
# from .views import create_adds, list_adds, delete_adds, edit_adds

urlpatterns = [
    # pedidos
    path('create_order/', create_order, name='create_order'),
    path('list_user_orders/<str:cpf>', list_user_orders, name='list_user_orders'),
    path('list_restaurant_orders/<str:cnpj>', list_restaurant_orders, name='list_restaurant_orders'),
    path('list_status/', list_status, name='list_status'),
    path('list_items/', list_items, name='list_items'),
    path('list_all_orders/', list_all_orders, name='list_all_orders'),

    # path('list_orders/', list_orders, name='list_orders'),
    # path('edit_order/<int:number_identification>', edit_order, name='edit_order'),
    # path('delete_order/<int:number_identification>', delete_order, name='delete_order'),
    # adicionais
    # path('create_adds/', create_adds, name='create_adds'),
    # path('list_adds/', list_adds, name='list_adds'),
    # path('edit_adds/<int:adds_number_identification>', edit_adds, name='edit_adds'),
    # path('delete_adds/<int:adds_number_identification>', delete_adds, name='delete_adds')
]
