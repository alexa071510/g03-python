from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from meseros.forms import MeseroForm
from meseros.models import Mesero
from datetime import date

# Serializador
from django.core import serializers as ssr

# DRF

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from meseros.serializers import MeseroSerializer


# Create your views here.
def meseros_list(request):

    #meseros=Mesero.objects.all()

    query = Q(nacionalidad__startswith='Per') & ~Q(edad__gt=30)
    meseros = Mesero.objects.filter(query)

    return render(request, 'meseros/meseros_list.html', context={'data':meseros})

def meseros_details(request):
    """Obtener todos los elementos de una tabla en la BD"""
    meseros = Mesero.objects.all()
    return render(request, 'meseros/meseros_details.html', context={'data': meseros})

#vistas basadas en clases

class MeseroList(ListView):
    #permission_classes = [IsAuthenticated]
    model = Mesero
    template_name = 'meseros/meseros_vc.html'


class MeseroCreate(CreateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/meseros_create.html'
    success_url = reverse_lazy('meseros_list_vc')


class MeseroUpdate(UpdateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/meseros_update_vc.html'
    success_url = reverse_lazy('meseros_list_vc')


class MeseroDelete(DeleteView):
    model = Mesero
    success_url = reverse_lazy('meseros_list_vc')
    template_name = 'meseros/meseros_confirm_delete.html'

"""Serializers"""

def ListMeseroSerializer(request):
    lista = ssr.serialize('json', Mesero.objects.all(), fields=['nombre', 'nacionalidad', 'edad'])
    return HttpResponse(lista, content_type="application/json")

"""Vistas creadas con Django Rest Framework"""

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def mesero_api_view(request):

    if request.method == 'GET':
        queryset = Mesero.objects.all()  # Se obtiene todos los datos de la tabla mesero
        serializers_class = MeseroSerializer(queryset, many=True)

        return Response(serializers_class.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MeseroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def mesero_detail_view(request, pk):
    mesero = Mesero.objects.filter(id=pk).first()

    if mesero:
        if request.method == 'GET':
            serializers_class = MeseroSerializer(mesero)
            return Response(serializers_class.data)

        elif request.method == 'PUT':
            serializers_class = MeseroSerializer(mesero, data=request.data)

            if serializers_class.is_valid():
                serializers_class.save()
                return Response(serializers_class.data)
            return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            mesero.delete()
            return Response('Mesero se ha eliminado correctamente', status=status.HTTP_201_CREATED)
    return Response({'message': 'No se ha encontrado ningún mesero con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
