from django.test import TestCase
from .models import Order, Adds
from rest_framework.test import APITestCase
import json
from django.core import serializers
from .serializers import OrderSerializer
from .order_test_helper import create_order, create_adds
from .order_test_helper import (default_description, default_name, 
                                default_number_identification, default_pk, 
                                default_quantity, adds_name, adds_number_identification, 
                                adds_quantity, adds_description, adds_pk)

class CheckOrderAPITest(APITestCase):

    def test_create_order_with_correct_params(self):
        data = create_order(default_name, default_number_identification, default_description, default_quantity)
        response = self.client.post('/create_order/', data=data)
        self.assertEqual(response.status_code, 200)


    def test_delete_order_with_wrong_id(self):
        data = create_order(default_name, default_number_identification, default_pk, default_quantity)
        response = self.client.post('/delete_order/', data=data)
        self.assertEqual(response.status_code, 404)


    def test_list_orders(self):
        data = create_order(default_name, default_number_identification , default_pk, default_quantity)
        response_1 = self.client.post('/create_order/', data=data)
        self.assertEqual(response_1.status_code, 200)

        response_2 = self.client.post('/list_orders/', data=data)
        self.assertEqual(response_2.status_code, 200)


    def test_edit_order_with_missing_params(self):
        data = create_order(default_name, '' , default_pk, default_quantity)
        response_2 = self.client.post('edit_order/', data=data)
        self.assertEqual(response_2.status_code, 404)


class CheckOrderAdds(APITestCase):

    def test_create_adds_with_correct_adds(self):
        data_adds = create_adds(adds_name, adds_number_identification, adds_description, adds_quantity)
        response = self.client.post('/create_adds/', data_adds=data_adds)
        self.assertEqual(response.status_code, 200)


    def test_create_adds_with_status_0(number_identification, status=0):
        Adds.objects.create(
            adds_name = adds_name,
            adds_description = adds_description,
            adds_quantity = adds_quantity,
            adds_number_identification = adds_number_identification)


    def test_delete_adds_with_wrong_id(self):
        data = create_order(adds_name, adds_number_identification, adds_pk, adds_quantity)
        response = self.client.post('/delete_adds/', data=data)
        self.assertEqual(response.status_code, 404)


    def test_list_adds(self):
        request_1 = {}
        response_1 = self.client.post('/list_adds/', request_1)
        self.assertEqual(response_1.status_code, 200)


    def test_edit_order_with_missing_params_to_adds(self):
        request_1 = {'adds_name': 'test_order', 'adds_description': 'some description', 'adds_quantity': '2'}
        response_1 = self.client.post('edit_adds/', request_1)
        self.assertEqual(response_1.status_code, 404)
    
