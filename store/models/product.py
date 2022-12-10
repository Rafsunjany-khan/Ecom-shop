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
     def get_all_products():
          return Product.objects.all()