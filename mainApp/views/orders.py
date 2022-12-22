from django.shortcuts import render, redirect
from mainApp.models.orders import Order
from django.views import View

class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_order_by_customer(customer)
        return render(request, 'order.html', {'orders': orders})
