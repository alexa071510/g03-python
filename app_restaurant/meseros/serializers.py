from rest_framework import serializers

from meseros.models import Mesero


class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesero
        fields = ('nombre', 'nacionalidad','edad')