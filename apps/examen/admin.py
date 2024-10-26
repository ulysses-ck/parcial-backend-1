from django.contrib import admin
from .models import Examen, AsignacionExamen
# Register your models here.
@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha_creacion',
'asignatura',
'profesor')
    
@admin.register(AsignacionExamen)
class AsignacionExamenAdmin(admin.ModelAdmin):
    list_display = (
 "alumno",
 "examen", "calificacion",
 "observacion",
 "estado",
 "fecha_creacion",
 "fecha_resolucion",
)