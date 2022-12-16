from django.shortcuts import render
from .models.product import *
from .models.customer import Customer
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


    data = {}
    data['products'] = products
    data['category'] = category
    return render(request, 'index.html', data)
def signUp(request):
    if request.method == 'GET':
        return render(request, 'store/signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone_no = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        customer = Customer(first_name=first_name, last_name=last_name, phone_no=phone_no, email=email, password=password)
        customer.register()
        return HttpResponse("Account Create Successfully")

def order(request):
    return render(request, 'order/order.html')