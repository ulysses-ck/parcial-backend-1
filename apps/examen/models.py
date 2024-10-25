from django.db import models
from ..asignaturas.models import Asignaturas
from ..alumnos.models import Alumnos
from ..profesores.models import Profesores
# Create your models here.
class Examen(models.Model):
    fecha_creacion = models.DateField()
    asignatura = models.ForeignKey(Asignaturas,on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesores,on_delete=models.CASCADE)

class AsignacionExamen(models.Model):
    alumno = models.ForeignKey(Alumnos,on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen,on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    observacion = models.CharField(max_length=100)
    estado = models.BooleanField()
    fecha_creacion = models.DateField()
    fecha_resolucion = models.DateField()




