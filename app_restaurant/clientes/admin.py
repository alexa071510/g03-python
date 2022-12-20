from django.contrib import admin
from .models import Cliente

# Register your models here.
#admin.site.register(Catalog)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','dni')
    search_fields = ('dni',)