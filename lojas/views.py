from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Produto, Carrinho, Pedido
from .helpers import CriadorPedido


def index(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'lojas/index.html', context)


def detail(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'lojas/detail.html', {'produto': produto})


def add_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho = Carrinho.objects.get(pk=1)
    quantidade = request.POST['quantidade']
    carrinho.adicionar_produto(produto, quantidade)
    return HttpResponseRedirect(reverse('lojas:carrinho'))


def carrinho(request):
    carrinho = Carrinho.objects.get(pk=1)
    itens = carrinho.itens_carrinho.all()
    return render(request, 'lojas/carrinho.html', {'itens': itens})


def finalizar_compra(request):
    carrinho = Carrinho.objects.get(pk=1)
    criador_pedido = CriadorPedido(carrinho)

    if criador_pedido.save():
        return HttpResponseRedirect(reverse('lojas:pedidos'))
    else:
        msg = "Nao foi possivel fechar a compra %s" % criador_pedido.string_errors()
        return render(request, 'lojas/carrinho.html', {'itens': carrinho.itens_carrinho.all(), 'msg': msg})


def pedidos(request):
    pedidos_usuario = Pedido.objects.all()
    return render(request, 'lojas/pedidos/index.html', {'pedidos': pedidos_usuario})
