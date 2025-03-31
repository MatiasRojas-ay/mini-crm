from django.db import models
from clientes.models import Cliente

class Presupuesto(models.Model):
    ESTADOS = [
        ('enviado', 'Enviado'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='enviado')
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Presupuesto #{self.id} - {self.cliente.nombre}"

class Pago(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    metodo = models.CharField(max_length=50)

    def __str__(self):
        return f"${self.monto} - {self.metodo} ({self.fecha})"
