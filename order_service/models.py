from django.db import models

# Create your models here.

class Order(models.Model):

    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 100)
    quantity = models.IntegerField()
    price = models.FloatField()
    number_identification = models.IntegerField(primary_key = True)
    

class AditionalItems(models.Model):
    
    additional_quantity = models.IntegerField()
    additional_price = models.FloatField()
    additional_description = models.TextField(max_length = 100)
