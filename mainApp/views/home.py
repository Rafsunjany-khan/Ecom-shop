from django.shortcuts import render
from mainApp.models.product import Product
from mainApp.models.category import Category


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
    print('you are: ', request.session.get('email'))
    return render(request, 'index.html', data)
