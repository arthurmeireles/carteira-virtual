from django.db import models

# Create your models here.
class Compra(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    parcelas = models.IntegerField()
    def __str__(self):
        return self.nome

class Cartao(models.Model):
    nome = models.CharField(max_length=255)
    limite = models.FloatField()
    compras = models.ForeignKey(Compra, on_delete=models.CASCADE)

class Entrada(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField()