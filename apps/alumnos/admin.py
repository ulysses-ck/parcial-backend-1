from django.contrib import admin
from ..alumnos.models import Alumnos
# Register your models here.
@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','email','asignatura','dni')

