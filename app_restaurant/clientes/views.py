from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from datetime import date

from clientes.forms import ClienteForm
from clientes.models import Cliente

# Serializador
from django.core import serializers as ssr


# Create your views here.
def clientes_list(request):

    #clientes=Cliente.objects.all()

    query = Q(nombre__startswith='Jac')
    clientes = Cliente.objects.filter(query)

    return render(request, 'clientes/clientes_list.html', context={'data':clientes})

def clientes_details(request):
    """Obtener todos los elementos de una tabla en la BD"""
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes_details.html', context={'data': clientes})

#vistas basadas en clases

class ClienteList(ListView):
    #permission_classes = [IsAuthenticated]
    model = Cliente
    template_name = 'clientes/clientes_vc.html'


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/clientes_create.html'
    success_url = reverse_lazy('meseros_list_vc')


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/clientes_update_vc.html'
    success_url = reverse_lazy('clientes_list_vc')


class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes_list_vc')
    template_name = 'clientes/clientes_confirm_delete.html'

