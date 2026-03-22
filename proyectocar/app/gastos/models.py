from django.db import models
from app.personas.models import Persona

class Gasto(models.Model):
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    fecha = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    imagengasto = models.ImageField(upload_to='gastos', blank=True, null=True)

    def __str__(self):
        return self.descripcion
