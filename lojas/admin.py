from django.contrib import admin

from .models import Produto, Carrinho, Pedido

admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(Pedido)
