from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Persona
from app.gastos.models import Gasto # Asegúrate de que esta ruta de importación sea correcta

class Home(TemplateView):
    template_name = "inicio.html"

class addPersonas(CreateView):
    model = Persona
    template_name = "agregarPersonas.html"
    fields = "__all__"
    success_url = reverse_lazy('inicio')

class addGastos(CreateView):
    model = Gasto
    template_name = "agregarGastos.html"
    fields = "__all__"
    success_url = reverse_lazy('iniciogastos')