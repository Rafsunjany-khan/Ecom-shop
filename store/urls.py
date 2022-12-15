from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    #path('<id>', views.store, name='store'),
    path('order/', views.order, name='order'),
]