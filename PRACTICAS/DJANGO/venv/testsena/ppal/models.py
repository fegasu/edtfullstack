from django.db import models

# Create your models here.
from unittest.util import _MAX_LENGTH
class PROYECTOS(models.Model):
    nom=models.TextField()
    descripcion=models.TextField()
    prefijo=models.CharField(max_length=4)
    activo=models.IntegerField()
class PLATAFORMAS(models.Model):
    nom=models.TextField()
    estado=models.IntegerField()
class REQUERIMIENTOS(models.Model):
    nom=models.TextField()
    descripcion=models.TextField()
    estado=models.IntegerField()
    tipo=models.IntegerField()
    idplan=models.IntegerField()
class ROLES(models.Model):
    nom=models.TextField()
    estado=models.IntegerField()

        
#python manage.py makemigrations ppal
#python manage.py migrate