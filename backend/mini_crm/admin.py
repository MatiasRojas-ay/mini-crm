from clientes.models import Cliente
from proyectos.models import Proyecto, Tarea, Responsable
from presupuestos.models import Presupuesto, Pago


def dashboard_callback(request, context):
    """
    Dashboard personalizado para Unfold.
    """
    total_clientes = Cliente.objects.count()
    total_proyectos = Proyecto.objects.count()
    total_tareas = Tarea.objects.count()
    total_presupuestos = Presupuesto.objects.count()
    total_pagos = Pago.objects.count()

    context.update({
        "kpis": [
            {"title": "Clientes", "metric": total_clientes},
            {"title": "Proyectos", "metric": total_proyectos},
            {"title": "Tareas", "metric": total_tareas},
            {"title": "Presupuestos", "metric": total_presupuestos},
            {"title": "Pagos", "metric": total_pagos},
        ],
    })
    return context