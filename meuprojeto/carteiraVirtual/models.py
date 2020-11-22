from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Carteira(models.Model):
    dono = models.ForeignKey(User, on_delete = models.CASCADE)
    saldo = models.IntegerField

class Cartao(models.Model):
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    limiteCredito = models.IntegerField
    saldoDebito = models.IntegerField

class CompraCartao(models.Model):
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    cartao = models.ForeignKey(Cartao, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    valor = models.IntegerField
    autor = models.CharField(max_length=255)
    pacelas = models.IntegerField


class CompraCarteira(models.Model):
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    valor = models.IntegerField
    autor = models.CharField(max_length=255)
    
