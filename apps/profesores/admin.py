from django.contrib import admin
from .models import Profesores
# Register your models here.
@admin.register(Profesores)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','email')