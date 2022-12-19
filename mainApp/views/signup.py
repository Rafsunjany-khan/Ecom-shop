from django.shortcuts import render, redirect
from mainApp.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class SignUp(View):
    def get(self, request):
        return render(request, 'store/signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone_no = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_no': phone_no,
            'email': email,
        }

        customer = Customer(first_name=first_name, last_name=last_name, phone_no=phone_no, email=email,
                            password=password)
        # validation
        error_msg = self.validateCustomer(customer)
        # save data
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            context = {
                'error': error_msg,
                'value': values,
            }
            return render(request, 'store/signup.html', context)

    def validateCustomer(self, customer):
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
