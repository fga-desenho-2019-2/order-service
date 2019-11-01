from django.test import TestCase
from .models import Order
from rest_framework.test import APITestCase
import json
from django.core import serializers
from .serializers import OrderSerializer
from .order_test_helper import create_order
from .order_test_helper import (default_description, default_name, 
                                default_number_identification, default_pk, default_quantity)

class CheckOrderAPITest(APITestCase):

    def test_create_order_with_correct_params(self):
        # If the order was successfully created
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

    def test_create_order_with_correct_adds(self):
        request_1 = {'adds_name':'brocolis', 'adds_number_identification':'1', 'adds_description':'Descrição topzera', 'adds_quantity':'2'}
        response_1 = self.client.post('/create_adds/', request_1)
        self.assertEqual(response_1.status_code, 200)

    def test_delete_adds_with_wrong_id(self):
        request_1 = {'adds_number_identification': '1', 'adds_name': 'Bad name', 'adds_description': 'Bad description', 'adds_quantity': '2'}
        self.client.post('/delete_adds/', request_1)

        # INTERNAL REQUEST ERROR if order does not exist
        request_2 = {'number_identification': 'p'}
        response_2 = self.client.post('/delete_adds/', request_2)
        self.assertEqual(response_2.status_code, 404)

    def test_list_adds(self):
        request_1 = {}
        response_1 = self.client.post('/list_adds/', request_1)
        self.assertEqual(response_1.status_code, 200)

    def test_edit_order_with_missing_params_to_adds(self):
        request_1 = {'adds_name': 'test_order', 'adds_description': 'some description', 'adds_quantity': '2'}
        response_1 = self.client.post('edit_adds/', request_1)
        self.assertEqual(response_1.status_code, 404)
    
