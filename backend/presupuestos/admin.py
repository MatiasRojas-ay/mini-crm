from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Presupuesto, Pago

@admin.register(Presupuesto)
class PresupuestoAdmin(ModelAdmin):
    list_display = ("id", "cliente", "monto_total", "estado", "fecha_creacion", "fecha_vencimiento")
    list_filter = ("estado", "fecha_creacion")
    search_fields = ("cliente__nombre",)

@admin.register(Pago)
class PagoAdmin(ModelAdmin):
    list_display = ("presupuesto", "monto", "fecha", "metodo")
    list_filter = ("metodo", "fecha")