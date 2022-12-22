from django.urls import path
from . import views
from .views import home, signup, login, cart
from .views.login import logout
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import authen_middleware

urlpatterns = [
    path('', home.Homepage.as_view(), name='homepage'),
    path('signup/', signup.SignUp.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', logout , name='logout'),
    path('cart/', cart.Cart.as_view(), name='cart'),
    path('checkout/', CheckOut.as_view(), name='checkout'),
    path('order/', authen_middleware(OrderView.as_view()), name='order'),

]
