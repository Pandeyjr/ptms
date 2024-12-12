# route_manager/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.route_manager_login, name='route_manager_login'),
    path('', views.route_manager_home, name='route_manager_home'),
    path('api/get_route/<int:route_id>/', views.get_route, name='get_route'), 
    path('create_route/', views.create_route, name='create_route'),


]
