from django.forms import ModelForm

from platos.models import Plato


class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ('nombre', 'procedencia', 'precio')

