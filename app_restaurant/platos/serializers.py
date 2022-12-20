from rest_framework import serializers

from platos.models import Plato


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = ('nombre', 'procedencia','precio')