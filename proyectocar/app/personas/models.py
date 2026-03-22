from django.db import models
from django.contrib import admin


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    parentesco = models.CharField(max_length=100, null=True, blank=True)
    ocupacion = models.CharField(max_length=100, null=True, blank=True)
    datos_medicos = models.CharField(max_length=250, null=True, blank=True)
    ingreso_mensual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gastos_mensuales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    foto = models.ImageField(upload_to='personas/', null=True, blank=True)

    def __str__(self):
        return self.Nombres
