from django.test import TestCase
from .models import Order
from rest_framework.test import APITestCase
import json
from django.core import serializers
from .serializers import OrderSerializer
from .order_test_helper import create_order


default_name = "Good name"
default_number_identification = 1
default_quantity = 2
default_description = "Good description"
default_pk = 1


class CheckOrderAPITest(APITestCase):

    def test_create_order_with_correct_params(self):
        # If the order was successfully created
        data = create_order(default_name, default_number_identification, default_description, default_quantity)
        response = self.client.post('/create_order/', data=data)
        self.assertEqual(response.status_code, 200)


    def test_create_order_with_status_0(number_identification, status=0):

        Order.objects.create(
            name = default_name,
            description = default_description,
            quantity = default_quantity,
            number_identification = default_number_identification)


    def test_delete_order_with_right_params(self):
<<<<<<< HEAD
        pk = default_number_identification 
=======
        pk = default_number_identification
>>>>>>> 33a50cbe48ba4789df91225180882890c6cc8371

        data = create_order(default_name, default_number_identification, default_description, default_quantity)
        response = self.client.post('/create_order/', data=data)
        self.assertEqual(response.status_code, 200)

        data2 = {}
        response2 = self.client.post('/list_orders/', data2)
        self.assertEqual(response2.status_code, 200)

        data3 = {'default_number_identification': data2}
        response3 = self.client.post('/delete_order/', data=data3, format='json')
        self.assertEqual(response3.status_code, 404)


    def test_delete_order_with_unmatching_id(self):
        request_2 = {'number_identification': 'p'}
        response_2 = self.client.post('/delete_order/', request_2)
        self.assertEqual(response_2.status_code, 404)


    def test_list_orders(self):
        request_1 = {}
        response_1 = self.client.post('/list_orders/', request_1)
        self.assertEqual(response_1.status_code, 200)


    def test_edit_order_with_missing_params(self):
        request_1 = {'name': 'test_order', 'description': 'test_description', 'quantity': '2'}
        response_1 = self.client.post('edit_order/', request_1)
        self.assertEqual(response_1.status_code, 404)


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
    
