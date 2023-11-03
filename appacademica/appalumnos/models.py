from django.db import models

# Create your models here.
class alumno(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=65)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=9)

class materia(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=65)
    uv = models.SmallIntegerField(max_length=2)

class docente(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=65)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=9)