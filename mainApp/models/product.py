from django.db import models
from .category import Category

class Product(models.Model):
     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
     name = models.CharField(max_length=800)
     color = models.CharField(max_length=50)
     price = models.IntegerField(default=0)
     description = models.CharField(max_length=800, default='')
     image = models.ImageField(upload_to='Image/product')

     @staticmethod
     def get_products_by_id(ids):
          return Product.objects.filter(id__in = ids)

     @staticmethod
     def get_products_by_id(ids):
          return Product.objects.filter(id__in=ids)

     @staticmethod
     def get_all_products():
          return Product.objects.all()

     @staticmethod
     def get_all_products_by_category_id(category_id):
          if category_id:
               return Product.objects.filter(category = category_id)
          else:
               return Product.get_all_products();