#from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
    path('menu', views.menu, name='menu'),
    path('reporte_clientes', views.reporte_clientes, name='reporte_cliente'),
    path('home', views.home, name='home'),

]