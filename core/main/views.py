from django.shortcuts import render
from products.views import Product

def index(request):
    products = Product.objects.all()[0:5]
    return render(request, "main/index.html", {'products':products})