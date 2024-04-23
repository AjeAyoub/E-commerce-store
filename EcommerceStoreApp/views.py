from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    return render(request, 'pages/store.html', context)

def cart(request):
    context = {}
    return render(request, 'pages/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'pages.checkout.html', context)