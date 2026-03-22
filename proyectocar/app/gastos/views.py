from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.db.models import Sum, Q
from datetime import datetime, timedelta
from .models import Gasto
from .forms import GastoForm
from app.personas.models import Persona

class Home(TemplateView):
    template_name = "inicio.html"

class addGastos(CreateView):
    model = Gasto
    template_name = "agregarGastos.html"
    form_class = GastoForm
    success_url = reverse_lazy('ver_gastos')

def inicio(request):
    return render(request, 'inicio.html')

def ver_gastos(request):
    gastos = Gasto.objects.all()
    return render(request,'verGastos.html',{
        'gastos':gastos
    })

def reportes_mensuales(request):
    """Vista para mostrar reportes mensuales de gastos"""
    gastos = Gasto.objects.all().order_by('-fecha')
    
    # Agrupar por mes y año
    meses_gastos = {}
    for gasto in gastos:
        mes_año = gasto.fecha.strftime('%Y-%m')
        if mes_año not in meses_gastos:
            meses_gastos[mes_año] = {
                'mes': gasto.fecha.strftime('%B %Y'),
                'gastos': [],
                'total': 0
            }
        meses_gastos[mes_año]['gastos'].append(gasto)
        meses_gastos[mes_año]['total'] += float(gasto.monto)
    
    # Calcular total anual
    total_anual = gastos.aggregate(total=Sum('monto'))['total'] or 0
    
    # Información de ingresos
    personas = Persona.objects.all()
    total_ingresos = sum(p.ingreso_mensual or 0 for p in personas)
    total_gastos_personas = sum(p.gastos_mensuales or 0 for p in personas)
    
    contexto = {
        'meses_gastos': sorted(meses_gastos.items(), reverse=True),
        'total_anual': total_anual,
        'total_ingresos': total_ingresos,
        'total_gastos_personas': total_gastos_personas,
        'saldo_total': total_ingresos - total_anual
    }
    
    return render(request, 'reportesMensuales.html', contexto)

def reportes_personas(request):
    """Vista para mostrar reportes por persona"""
    personas = Persona.objects.all()
    
    datos_personas = []
    for persona in personas:
        # Gastos asignados a esta persona
        gastos_persona = Gasto.objects.filter(persona=persona).aggregate(total=Sum('monto'))['total'] or 0
        cantidad_gastos = Gasto.objects.filter(persona=persona).count()
        ingreso = persona.ingreso_mensual or 0
        gastos_registrados = persona.gastos_mensuales or 0
        
        # Saldo
        saldo_ingreso = float(ingreso) - float(gastos_registrados)
        
        datos_personas.append({
            'persona': persona,
            'gastos_asignados': gastos_persona,
            'cantidad_gastos': cantidad_gastos,
            'ingreso_mensual': ingreso,
            'gastos_mensuales': gastos_registrados,
            'saldo': saldo_ingreso,
            'saldo_color': 'text-success' if saldo_ingreso >= 0 else 'text-danger'
        })
    
    # Totales generales
    total_ingresos = sum(p['ingreso_mensual'] for p in datos_personas)
    total_gastos = sum(p['gastos_mensuales'] for p in datos_personas)
    total_asignados = sum(p['gastos_asignados'] for p in datos_personas)
    saldo_general = total_ingresos - total_gastos
    
    contexto = {
        'datos_personas': datos_personas,
        'total_ingresos': total_ingresos,
        'total_gastos': total_gastos,
        'total_asignados': total_asignados,
        'saldo_general': saldo_general,
        'saldo_color': 'text-success' if saldo_general >= 0 else 'text-danger'
    }
    
    return render(request, 'reportesPersonas.html', contexto)