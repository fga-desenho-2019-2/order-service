from django.db import models

# Create your models here.

class OrderStatus(models.Model):
    STATUS_CHOICE = [
        ('INI', 'Iniciado'),
        ('CAN', 'Cancelado'),
        ('AND', 'Em andamento'),
        ('PROC', 'Em processamento'),
        ('PREP', 'Sendo preparado'),
        ('AGUARD', 'Aguardando retirada'),
        ('FIN', 'Finalizado'),
    ]
    description = models.CharField(
        max_length=6,
        choices=STATUS_CHOICE,
        default='INI'
    )

    def __str__(self):
        return self.description


class Order(models.Model):

    cpf_user = models.CharField(max_length=11)
    cod = models.CharField(max_length=20)
    cnpj_restaurant = models.CharField(max_length=16)
    value = models.FloatField()
    avaliation_description = models.CharField(max_length=200, blank=True, null=True)
    avaliation_number = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.CASCADE,
        related_name='status'
    )

    def __str__(self):
        return self.cod


class Item(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    observation = models.CharField(max_length=200)
    quantity = models.IntegerField()
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE,
        related_name='items'
    )

    def __str__(self):
        return self.name



