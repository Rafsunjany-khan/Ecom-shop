from django.shortcuts import render, redirect
from .models.product import *
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse

# Create your views here.
def homepage(request):
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
def validateCustomer(customer):
    error_msg = None
    if (not customer.first_name):
        error_msg = 'required first name'
    elif len(customer.first_name) < 4:
        error_msg = 'first name 4 character or more'
    if (not customer.last_name):
        error_msg = 'required last name'
    elif len(customer.last_name) < 4:
        error_msg = 'last name 4 character or more'
    if (not customer.phone_no):
        error_msg = 'required phone number'
    elif len(customer.phone_no) < 10:
        error_msg = 'phone number have at least 11 character'
    if (not customer.email):
        error_msg = 'required email'
    elif len(customer.email) < 6:
        error_msg = 'email have @ and .com '
        # cheke mail regisered or not
    elif customer.isExists():
        error_msg = 'Email address already regiser'
    if (not customer.password):
        error_msg = 'required password'
    elif len(customer.password) < 5:
        error_msg = 'password length 6 character or more'
    return error_msg

def registerUser(request):
    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone_no = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')


    values =  {
        'first_name' : first_name,
        'last_name' : last_name,
        'phone_no' : phone_no,
        'email' : email,
    }

    customer = Customer(first_name=first_name, last_name=last_name, phone_no=phone_no, email=email,
                            password=password)
        # validation
    error_msg = validateCustomer(customer)
            # save data
    if not error_msg:
        customer.password = make_password(customer.password)
        customer.register()
        return redirect(homepage)
    else:
        context = {
            'error': error_msg,
            'value': values,
        }
        return render(request, 'store/signup.html', context)

def signUp(request):
    if request.method == 'GET':
        return render(request, 'store/signup.html')
    else:
        return registerUser(request)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password =  request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect(homepage)
            else:
                error_msg = "Email or password incorrect!"

        else:
            error_msg = "Email or password incorrect!"
        return render(request, 'login.html', {'error': error_msg})

def order(request):
    return render(request, 'order/order.html')