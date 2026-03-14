from django.db import models
from app.gastos import *

class Persona(models.Model):
    Nombres = models.CharField(max_length=100)
    Año_de_Nacimiento = models.DateField()
    Parentesco_Familiar = models.CharField(max_length=100)
    Ocupacion = models.CharField(max_length=100)
    Datos_medicos = models.CharField(max_length=100)
    Ingreso_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Nombres
