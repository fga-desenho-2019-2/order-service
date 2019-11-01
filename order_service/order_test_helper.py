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


# default atributes
default_name = "Good name"
default_number_identification = 1
default_quantity = 2
default_description = "Good description"
default_pk = 1