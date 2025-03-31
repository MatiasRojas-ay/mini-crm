from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Proyecto, Tarea, Responsable


@admin.register(Responsable)
class ResponsableAdmin(ModelAdmin):
    list_display = ("nombre", "email")
    search_fields = ("nombre", "email")


@admin.register(Proyecto)
class ProyectoAdmin(ModelAdmin):
    list_display = ("nombre", "cliente", "estado", "presupuesto", "fecha_inicio", "fecha_fin")
    list_filter = ("estado",)
    search_fields = ("nombre", "cliente__nombre")

    fieldsets = (
        ("Información General", {
            "classes": ["tab"],
            "fields": ("nombre", "cliente", "estado"),
        }),
        ("Planificación y Presupuesto", {
            "classes": ["tab"],
            "fields": ("presupuesto", "fecha_inicio", "fecha_fin"),
        }),
    )


@admin.register(Tarea)
class TareaAdmin(ModelAdmin):
    list_display = ("titulo", "proyecto", "prioridad", "estado", "fecha_limite", "responsable")
    list_filter = ("prioridad", "estado")
    search_fields = ("titulo", "proyecto__nombre", "responsable__nombre")

    fieldsets = (
        ("Tarea", {
            "classes": ["tab"],
            "fields": ("titulo", "descripcion"),
        }),
        ("Planificación", {
            "classes": ["tab"],
            "fields": ("proyecto", "prioridad", "estado", "fecha_limite"),
        }),
        ("Responsable", {
            "classes": ["tab"],
            "fields": ("responsable",),
        }),
    )
