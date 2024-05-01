from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'pages/store.html', context)

def cart(request):
    context = {}
    return render(request, 'pages/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'pages/checkout.html', context)
