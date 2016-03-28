from django.contrib import admin

from .models import Produto, Carrinho

admin.site.register(Produto)
admin.site.register(Carrinho)