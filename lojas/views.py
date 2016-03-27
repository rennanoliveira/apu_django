from django.shortcuts import render

from .models import Produto

from django.http import HttpResponse


def index(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'lojas/index.html', context)

def detail(request, produto_id):
    return HttpResponse("Produto %s" % produto_id)

# Create your views here.
