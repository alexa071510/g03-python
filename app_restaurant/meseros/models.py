from django.db import models

# Create your models here.
class Mesero(models.Model):
    nombre = models.CharField(max_length=35)
    nacionalidad = models.CharField(max_length=30)
    edad = models.IntegerField()
