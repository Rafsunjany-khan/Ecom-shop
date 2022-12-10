from django.shortcuts import render
from .models.product import *
from django.http import HttpResponse

# Create your views here.
def store(request):
    products = Product.get_all_products()
    return render(request, 'index.html', {'products': products})