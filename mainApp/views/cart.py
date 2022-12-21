from django.shortcuts import render, redirect
from mainApp.models.product import Product
from django.views import View

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'cart_products': products})
