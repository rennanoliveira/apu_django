from django.conf.urls import url

from . import views

app_name = 'lojas'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signedin/$', views.signedin, name='signedin'),
    url(r'^carrinho/$', views.carrinho, name='carrinho'),
    url(r'^finalizar_compra/$', views.finalizar_compra, name='finalizar_compra'),
    url(r'^pedidos/$', views.pedidos, name='pedidos'),
    url(r'^(?P<produto_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<produto_id>[0-9]+)/add_produto/$', views.add_produto, name='add_produto'),
    url(r'^carrinho/remove_produto/$', views.remove_produto, name='remove_produto'),

]
