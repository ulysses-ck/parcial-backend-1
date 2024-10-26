from django.urls import path
from apps.alumnos.views import AlumnoView
urlpatterns = [
    path('alumno/',AlumnoView.as_view()),
]