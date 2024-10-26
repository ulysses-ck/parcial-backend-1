from django.views.generic import TemplateView
from apps.alumnos.models import Alumnos


# Create your views here.

class AlumnoView(TemplateView):
    template_name = "alumnos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alumnos"] = Alumnos.objects.all()
        return context
    
