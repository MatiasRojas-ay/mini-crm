from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)
    empresa = models.CharField(max_length=100, blank=True)
    notas = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
