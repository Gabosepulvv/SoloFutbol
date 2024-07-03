#from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),

    path('crud', views.crud, name='crud'), #esto es parte del crud parte 1
    path('clientesAdd', views.clientesAdd, name='clientesAdd'), #desde aqui ya no funciona
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>', views.clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),
]