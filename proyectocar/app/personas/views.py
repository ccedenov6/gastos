from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Persona
from django.shortcuts import render 

def login_view(request):
    """Vista para la página de inicio de sesión"""
    return render(request, 'login.html')

def registro_view(request):
    """Vista para la página de registro"""
    if request.method == 'POST':
        # Aquí iría la lógica para crear un nuevo usuario
        # Por ahora, solo renderizamos la página
        pass
    return render(request, 'registro.html')

class Home(TemplateView):
    template_name = "inicio.html"

class addPersonas(CreateView):
    model = Persona
    template_name = "agregarPersonas.html"
    fields = "__all__"
    success_url = reverse_lazy('inicio')


def ver_personas(request):

    personas = Persona.objects.all()

    return render(request,'verPersonas.html',{
        'personas':personas
    })