from django.db import models
from .statics.status import ORDER_STATUS 


class Order(models.Model):

    cpf_user = models.CharField(max_length=11)
    cod = models.CharField(max_length=20)
    cnpj_restaurant = models.CharField(max_length=16)
    value = models.FloatField()
    avaliation_description = models.CharField(max_length=200, blank=True, null=True)
    avaliation_number = models.IntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        choices=ORDER_STATUS,
        default=1
    )

    def __str__(self):
        return self.cod


class Item(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    observation = models.CharField(
        max_length=200,
        blank=True
    )
    quantity = models.IntegerField()
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE,
        related_name='items'
    )

    def __str__(self):
        return self.name



