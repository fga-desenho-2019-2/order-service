from django.db import models

# Create your models here.

class Order(models.Model):
    observation = models.CharField(max_length = 100)
    number_identification = models.IntegerField(primary_key = True)

class Adds(models.Model):

    adds_name = models.CharField(max_length = 50)
    adds_quantity = models.IntegerField()
    adds_description = models.TextField(max_length = 100)
    adds_number_identification = models.IntegerField(primary_key = True)

    def __str__(self):
        return self.adds_name + self.adds_description

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    quantity = models.IntegerField()