from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem vindo a lojinha")

# Create your views here.
