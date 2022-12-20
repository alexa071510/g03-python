from django.contrib import admin
from .models import Plato

# Register your models here.
#admin.site.register(Catalog)

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','procedencia')



