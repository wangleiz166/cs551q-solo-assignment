from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('userlist/', views.userList, name='userList'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('set_admin/<int:user_id>/', views.set_admin, name='set_admin'),   
    path('set_general/<int:user_id>/', views.set_general, name='set_general'),  
]