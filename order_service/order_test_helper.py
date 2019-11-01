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


def create_adds(adds_name = None, adds_quantity = None, adds_description = None, adds_number_identification = None, adds_pk = None):

    data_adds = {
        'adds_name': adds_name,
        'adds_quantity': adds_quantity,
        'adds_description': adds_description,
        'adds_number_identification': adds_number_identification,
        'adds_pk': adds_pk
    }

    return data_adds

# default atributes
default_name = "Good name"
default_number_identification = 1
default_quantity = 2
default_description = "Good description"
default_pk = 1

adds_name = "Queijo"
adds_quantity = 2
adds_description = "Put that cheese"
adds_number_identification = 1
adds_pk = 1