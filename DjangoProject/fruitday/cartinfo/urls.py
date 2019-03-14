from django.conf.urls import url
from fruitday.cartinfo import views

urlpatterns = [
    url(r'^$', views.cart_info, name='cart'),
    url(r'addcart', views.add_cart, name='addcart'),
    url(r'deletecart', views.delete_cart, name='deletecart'),
]