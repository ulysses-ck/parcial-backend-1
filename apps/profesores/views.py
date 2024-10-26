from django.views.generic import TemplateView
from apps.profesores.models import Profesores


# Create your views here.

class ProfesorView(TemplateView):
    template_name = "profesor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profesores"] = Profesores.objects.all()
        return context