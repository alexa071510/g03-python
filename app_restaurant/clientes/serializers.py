from rest_framework import serializers

from clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido','dni')