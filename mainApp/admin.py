from django.contrib import admin
from .models.product import Product
from .models.category import Category
from  .models.customer import Customer
from .models.orders import Order
class AdminProduct(admin.ModelAdmin):
    list_display = ['category' , 'name' , 'color' , 'price']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
