from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(ModelAdmin):
    list_display = ("nombre", "email", "telefono", "empresa")
    search_fields = ("nombre", "email", "empresa")
