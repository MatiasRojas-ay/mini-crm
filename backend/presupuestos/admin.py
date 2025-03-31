from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from django.urls import reverse
from .models import Presupuesto, Pago


@admin.register(Presupuesto)
class PresupuestoAdmin(ModelAdmin):
    list_display = ("id", "cliente", "monto_total", "estado", "fecha_creacion", "fecha_vencimiento", "ver_pdf")
    list_filter = ("estado", "fecha_creacion")
    search_fields = ("cliente__nombre",)

    fieldsets = (
        ("Cliente y Estado", {
            "classes": ["tab"],
            "fields": ("cliente", "estado"),
        }),
        ("Fechas y Monto", {
            "classes": ["tab"],
            "fields": ("monto_total", "fecha_creacion", "fecha_vencimiento"),
        }),
    )

    def ver_pdf(self, obj):
        url = reverse("presupuesto_pdf", args=[obj.pk])
        return format_html(f'<a class="button" href="{url}" target="_blank">📄 Descargar</a>')

    ver_pdf.short_description = "PDF"


@admin.register(Pago)
class PagoAdmin(ModelAdmin):
    list_display = ("presupuesto", "monto", "fecha", "metodo")
    list_filter = ("metodo", "fecha")

    fieldsets = (
        ("Información del Pago", {
            "classes": ["tab"],
            "fields": ("presupuesto", "monto", "fecha", "metodo"),
        }),
    )