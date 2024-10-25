from django.contrib import admin
from .models import Asignaturas
# Register your models here.
@admin.register(Asignaturas)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)