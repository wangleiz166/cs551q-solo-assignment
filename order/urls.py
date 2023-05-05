from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove_cart/<int:id>',views.remove_cart, name='remove_cart'),
]