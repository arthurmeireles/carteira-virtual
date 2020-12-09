from django.db import models

# Create your models here.
class Compra(models.Model):
    nome = models.CharField(max_length=255)


class Cartao(models.Model):
    nome = models.CharField(max_length=255)
    limite = models.IntegerField()
    compras = models.ForeignKey(Compra, on_delete=models.CASCADE)

