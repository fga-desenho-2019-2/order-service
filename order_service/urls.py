from django.urls import path
from django.conf.urls import url
from order_service import views
from .views import create_order, list_orders, edit_order, get_order


urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('list_orders/', list_orders, name='list_orders'),
    path('edit_order/', edit_order, name='edit_order'),
    path('get_order/', get_order, name='get_order')

]
