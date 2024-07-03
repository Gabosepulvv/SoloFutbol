from django.shortcuts import render
from clientes.models import Cliente
from django.contrib.auth.decorators import login_required
#from clientes.views import crud

# Create your views here.
@login_required
def menu(request):
    request.session["usuario"]=request.user.username
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'administrador/menu.html', context)

def reporte_clientes(request):
    clientes=Cliente.objects.all()
    context = {'clientes':clientes}
    return render(request, 'administrador/menu.html', context)


def home(request):
    context = {}
    return render(request, 'administrador/home.html', context)