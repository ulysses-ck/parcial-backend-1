from django.db import models

# Create your models here.

class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    asignatura = models.CharField(max_length=50)
    dni = models.IntegerField()




