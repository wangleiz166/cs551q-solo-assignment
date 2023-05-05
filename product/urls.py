from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.list, name='search'),
    path('list/', views.list, name='list'),
    path('detail/<str:id>', views.detail, name='detail')
]