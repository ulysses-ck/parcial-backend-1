from django.db import models

# Create your models here.
class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    asignatura = models.CharField(max_length=50)


