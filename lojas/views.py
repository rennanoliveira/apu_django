from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Produto, Carrinho, Pedido
from .helpers import CriadorPedido, PegaCarrinho
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'lojas/index.html', context)


@login_required()
def detail(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'lojas/detail.html', {'produto': produto})


@login_required()
def add_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho = PegaCarrinho(request.user).carrinho()
    quantidade = request.POST['quantidade']
    carrinho.adicionar_produto(produto, quantidade)
    return HttpResponseRedirect(reverse('lojas:carrinho'))


@login_required()
def remove_produto(request):
    item_id = request.POST['item_id']
    carrinho = PegaCarrinho(request.user).carrinho()
    item = get_object_or_404(carrinho.itens_carrinho, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('lojas:carrinho'))


@login_required()
def carrinho(request):
    carrinho = PegaCarrinho(request.user).carrinho()
    itens = carrinho.itens_carrinho.all()
    return render(request, 'lojas/carrinho.html', {'itens': itens})


@login_required()
def finalizar_compra(request):
    carrinho = PegaCarrinho(request.user).carrinho()
    criador_pedido = CriadorPedido(carrinho)

    if criador_pedido.save():
        return HttpResponseRedirect(reverse('lojas:pedidos'))
    else:
        msg = "Nao foi possivel fechar a compra %s" % criador_pedido.string_errors()
        return render(request, 'lojas/carrinho.html', {'itens': carrinho.itens_carrinho.all(), 'msg': msg})


@login_required()
def pedidos(request):
    pedidos_usuario = Pedido.objects.all()
    return render(request, 'lojas/pedidos/index.html', {'pedidos': pedidos_usuario})


@login_required()
def signedin(request):
    PegaCarrinho(request.user).carrinho()
    return HttpResponseRedirect(reverse('lojas:index'))

