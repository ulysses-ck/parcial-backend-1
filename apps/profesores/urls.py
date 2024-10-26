from django.urls import path
from apps.profesores.views import ProfesorView
urlpatterns = [
    path('profesor/',ProfesorView.as_view()),
]