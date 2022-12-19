from django.urls import path
from . import views
from .views import home, signup, login

urlpatterns = [
    path('', home.homepage, name='homepage'),
    path('signup/', signup.SignUp.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
]
