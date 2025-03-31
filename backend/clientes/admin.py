from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(ModelAdmin):
    list_display = ("nombre", "email", "telefono", "empresa")
    search_fields = ("nombre", "email", "empresa")

    fieldsets = (
        ("Información de Contacto", {
            "classes": ["tab"],
            "fields": ("nombre", "email", "telefono", "empresa"),
        }),
        ("Notas", {
            "classes": ["tab"],
            "fields": ("notas",),
        }),
    )
