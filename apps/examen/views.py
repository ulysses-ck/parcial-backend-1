from django.views.generic import TemplateView
from apps.examen.models import Examen


# Create your views here.

class ExamenView(TemplateView):
    template_name = "examen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examenes"] = Examen.objects.all()
        return context