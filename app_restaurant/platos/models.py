from django.db import models

# Create your models here.
class Plato(models.Model):
    nombre = models.CharField(max_length=35)
    precio = models.FloatField(default='')
    procedencia = models.CharField(max_length=25,default='')