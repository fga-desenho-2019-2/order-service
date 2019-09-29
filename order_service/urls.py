from django.urls import path
from django.conf.urls import url
from order_service import views
from .views import create_order, list_orders, delete_order, edit_order
from .views import create_adds, list_adds, delete_adds, edit_adds

urlpatterns = [
    # pedidos
    path('create_order/', create_order, name='create_order'),
    path('list_orders/', list_orders, name='list_orders'),
    path('edit_order/<int:number_identification>', edit_order, name='edit_order'),
    path('delete_order/<int:number_identification>', delete_order, name='delete_order'),
    # adicionais
    path('create_adds/', create_adds, name='create_adds'),
    path('list_adds/', list_adds, name='list_adds'),
    path('edit_adds/<int:adds_number_identification>', edit_adds, name='edit_adds'),
    path('delete_adds/<int:adds_number_identification>', delete_adds, name='delete_adds')
]
