from django.conf import settings
import requests

def create_order(name = None, number_identification = None, description = None, quantity = None):

    data = {
        'name': name,
        'number_identification': number_identification,
        'description': description,
        'quantity': quantity
    }

    return data