from django.urls import path
from django.conf.urls import url
from order_service import views
from .views import create_order, list_orders, delete_order, edit_order


urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('list_orders/', list_orders, name='list_orders'),
    path('edit_order/<int:number_identification>', edit_order, name='edit_order'),
    path('delete_order/<int:number_identification>', delete_order, name='delete_order')

]
