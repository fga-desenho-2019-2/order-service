from django.db import models

# Create your models here.

class Order(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length = 100)
    quantity = models.IntegerField()
    number_identification = models.IntegerField(primary_key = True)

    def __str__(self):
        return self.name


class AddsItens(models.Model):

    adds_name = models.CharField(max_length = 50)
    adds_quantity = models.IntegerField()
    adds_description = models.TextField(max_length = 100)
    adds_number_identification = models.IntegerField(primary_key = True)

    def __str__(self):
        return self.addition_name + self.addition_description