from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, ListView

from platos.forms import PlatoForm
from platos.models import Plato

# Serializador
from django.core import serializers as ssr

# Create your views here.
def platos_list(request):

    #platos = Plato.objects.all()
    query = Q(procedencia__startswith='Perú') & Q(precio__gt=40)
    platos = Plato.objects.filter(query)
    return render(request, 'platos/platos_list.html', context={'data':platos})

def platos_details(request):
    """Obtener todos los elementos de una tabla en la BD"""
    platos = Plato.objects.all()
    return render(request, 'platos/platos_details.html', context={'data':platos})

#vistas basadas en clases

class PlatoList(ListView):
    #permission_classes = [IsAuthenticated]
    model = Plato
    template_name = 'platos/platos_vc.html'


class PlatoCreate(CreateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'platos/platos_create.html'
    success_url = reverse_lazy('platos_list_vc')


class PlatoUpdate(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'platos/platos_update_vc.html'
    success_url = reverse_lazy('platos_list_vc')


class PlatoDelete(DeleteView):
    model = Plato
    success_url = reverse_lazy('platos_list_vc')
    template_name = 'platos/platos_confirm_delete.html'

"""Serializers"""

def ListPlatoSerializer(request):
    lista = ssr.serialize('json', Plato.objects.all(), fields=['nombre', 'procedencia', 'precio'])
    return HttpResponse(lista, content_type="application/json")
