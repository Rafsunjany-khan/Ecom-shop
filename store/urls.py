from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('signup/', views.signUp, name='signup'),
    path('order/', views.order, name='order'),
]