from django.db import models
from ..profesores.models import Profesores
from ..examen.models import Examen
from ..alumnos.models import Alumnos
# Create your models here.
class Asignaturas(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.ForeignKey(Profesores,on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen,on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumnos,on_delete=models.CASCADE)
