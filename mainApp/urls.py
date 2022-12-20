from django.urls import path
from . import views
from .views import home, signup, login
from .views.login import logout

urlpatterns = [
    path('', home.Homepage.as_view(), name='homepage'),
    path('signup/', signup.SignUp.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', logout , name='logout'),
]
