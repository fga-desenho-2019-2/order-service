from django.urls import path
from django.conf.urls import url
from order_service import views
from .views import order_serializer


urlpatterns = [
    path('register/', order_serializer, name='register'),

]
