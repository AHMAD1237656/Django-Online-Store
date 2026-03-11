from django.shortcuts import render
from .models import Product



def run_view(request):
    products = Product.objects.all()
    return render(request, 'run.html', {'products': products})

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})





