from django.db import models
from ..profesores.models import Profesores

# Create your models here.
class Asignaturas(models.Model):
    nombre = models.CharField(max_length=50)
    
