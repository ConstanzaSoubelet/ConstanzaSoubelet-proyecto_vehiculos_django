from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add', views.add_vehiculo, name='add_vehiculo'),
    path('vehiculo/list', views.listar_vehiculos, name='listar_vehiculos'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
