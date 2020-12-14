from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html')

def paginaInicial(request):
    compras = Compra.objects.all()
    form = ComprasForm
    context = {'compras': compras, 'form': form}
    return render(request, 'pages/paginaInicial.html', context)