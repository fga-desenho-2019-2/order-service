from django.test import TestCase
from ..api.models import Order
from rest_framework.test import APITestCase
import json
from django.core import serializers
from ..api.serializers import OrderSerializer

class CheckOrderAPITest(APITestCase):
    def setUp(self):
        self.data = {
            'cpf_user':'05333208107',
            'cnpj_restaurant':'33345811000183',
            'value':30.59,
            'items':[
            {
                'name':'Combo Big Mac',
                'value':22.19,
                'observation':'sem pão',
                'quantity':1
            }],
            'status': 1
        }

    def test_create_order_with_correct_params(self):
        response = self.client.post('/api/create_order/', data=self.data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_order_with_wrong_params(self):
        data = {
            'cnpj_restaurant':'33345811000183',
            'value':30.59,
            'items':[
            {
                'name':'Combo Big Mac',
                'value':22.19,
                'observation':'sem pão',
                'quantity':1
            }]
        }
        response = self.client.post('/api/create_order/', data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_list_user_orders(self):
        self.client.post('/api/create_order/', data=self.data)
        response_get = self.client.get('/api/list_user_orders/05333208107/1')
        self.assertEqual(response_get.status_code, 200)

    def test_list_restaurant_orders(self):
        self.client.post('/api/create_order/', data=self.data)
        response_get_restaurant = self.client.get('/api/list_restaurant_orders/33345811000183/1')
        self.assertEqual(response_get_restaurant.status_code, 200)

    # def test_update_status_order(self):
    #     self.client.post('/api/create_order/', data=self.data, format='json')
    #     response_put_order_status = self.client.put('/api/update_status_order/1/1', format='json')
    #     self.assertEqual(response_put_order_status.status_code, 200)        