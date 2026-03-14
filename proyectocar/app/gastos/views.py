from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Gasto

class Home(TemplateView):
    template_name = "iniciogastos.html"

def inicio(request):
    return render(request, 'inicio.html')