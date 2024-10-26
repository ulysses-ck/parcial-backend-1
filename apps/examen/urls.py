from django.urls import path
from apps.examen.views import ExamenView
urlpatterns = [
    path('examen/',ExamenView.as_view()),
]