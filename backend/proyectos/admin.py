from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(ModelAdmin):
    list_display = ("nombre", "cliente", "estado", "fecha_inicio", "fecha_fin")
    list_filter = ("estado",)
    search_fields = ("nombre", "cliente__nombre")

@admin.register(Tarea)
class TareaAdmin(ModelAdmin):
    list_display = ("titulo", "proyecto", "prioridad", "estado", "fecha_limite")
    list_filter = ("prioridad", "estado")
    search_fields = ("titulo", "proyecto__nombre")
