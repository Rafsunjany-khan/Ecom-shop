from django.shortcuts import render, redirect
from mainApp.models.product import Product
from mainApp.models.customer import Customer
from mainApp.models.orders import Order
from django.views import View

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone_no')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(customer = Customer(id = customer),
                          product = product,
                          price = product.price,
                          address = address,
                          phone_no = phone,
                          quantity = cart.get(str(product.id))
                          )
            order.placeOrder()
        request.session['cart'] = {}

        return redirect('cart')
