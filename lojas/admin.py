from django.contrib import admin

from .models import Produto, Carrinho, Pedido, ItemCarrinho, StatusPedido

admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(Pedido)
admin.site.register(ItemCarrinho)
admin.site.register(StatusPedido)

