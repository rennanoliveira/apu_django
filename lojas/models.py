from __future__ import unicode_literals

from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    def remover_estoque(self, quantidade):
        self.quantidade -= int(quantidade)
        self.save()

    def __str__(self):
        return self.nome + ' - R$ ' + "%01.2f" % self.preco + ' (' + str(self.quantidade) + ')'


class Carrinho(models.Model):
    def adicionar_produto(self, produto, quantidade):
        try:
            item = self.itens_carrinho.get(pk=produto.id)
        except ItemCarrinho.DoesNotExist:
            item = ItemCarrinho(carrinho=self, produto=produto, quantidade=0)
        item.quantidade += int(quantidade)
        item.save()
        return item

    def qtd_itens(self):
        return self.itens_carrinho.count()

    def custo_total(self):
        total = float(0)
        for item in self.itens_carrinho.all():
            total += float(item.produto.preco)
        return float(total)

    def __str__(self):
        return "(id: %d) %d produtos, total: R$ %s" % (self.id, self.qtd_itens(), ("%01.2f" % self.custo_total()))


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="itens_carrinho")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return self.produto.nome + ' (' + str(self.quantidade) + ')'


class Pedido(models.Model):
    status = models.CharField(max_length=200, default='aguardando pagamento')

    def qtd_itens(self):
        return self.itens_pedido.count()

    def custo_total(self):
        total = float(0)
        for item in self.itens_pedido.all():
            total += float(item.produto.preco)
        return float(total)

    def __str__(self):
        return "(id: %d) %d produtos, total: R$ %s" % (self.id, self.qtd_itens(), ("%01.2f" % self.custo_total()))


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens_pedido")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return "Pedido %d: %d produtos, total: R$ %s" % (self.id, self.qtd_itens(), ("%01.2f" % self.custo_total()))

        return "(id: %d) %d produtos, total: R$ %s" % (self.id, self.qtd_itens(), ("%01.2f" % self.custo_total()))

