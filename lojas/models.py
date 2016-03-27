from __future__ import unicode_literals

from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField()


class Carrinho(models.Model):
    pass


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()


class Pedido(models.Model):
    status = models.CharField(max_length=200)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quandidade = models.IntegerField()





