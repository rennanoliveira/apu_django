from __future__ import unicode_literals

from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=1)
    def __str__(self):
        return self.nome + ' (' + str(self.quantidade) + ')'


class Carrinho(models.Model):
    def __str__(self):
        return self.id


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    def __str__(self):
        return self.produto.nome + ' (' + str(self.quantidade) + ')'


class Pedido(models.Model):
    status = models.CharField(max_length=200)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quandidade = models.IntegerField(default=1)
    def __str__(self):
        return "Pedido %d; produto: %s; quantidade: %d" % (self.pedido.id,self.produto.nome,self.quantidade)




