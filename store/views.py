from django.shortcuts import render
from .models.product import *
from django.http import HttpResponse

# Create your views here.
def store(request):
    products = None
    category = Category.get_all_category()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_category_id(categoryID)
    else:
        products = Product.get_all_products()
    print(products)

    data = {}
    data['products'] = products
    data['category'] = category
    return render(request, 'index.html', data)
def order(request):
    return render(request, 'order/order.html')