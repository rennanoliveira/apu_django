from .models import Pedido, Produto, ItemPedido


class CriadorPedido:
    def __init__(self, carrinho):
        self.carrinho = carrinho
        self.errors = []

    def save(self):
        itens_no_carrinho = self.carrinho.itens_carrinho.all()
        return (self.verifica_itens(itens_no_carrinho) and self.fechar_pedido(itens_no_carrinho))

    def verifica_itens(self, itens):
        for item in itens:
            produto = Produto.objects.get(pk=item.produto_id)
            if (produto.quantidade < item.quantidade):
                erro = "Quantidade solicitada (%s) do produto '%s' menor que a quantidade em estoque (%s)" % (
                item.quantidade, produto.nome, produto.quantidade)
                self.errors.append(erro)

        return len(self.errors) == 0

    def fechar_pedido(self, itens):
        pedido = Pedido()
        pedido.save()
        for item in itens:
            produto = item.produto
            item_pedido = ItemPedido(pedido=pedido, produto=produto, quantidade=item.quantidade)
            item_pedido.save()
            produto.remover_estoque(item.quantidade)
        self.carrinho.limpar()
        pedido.save()
        return True
