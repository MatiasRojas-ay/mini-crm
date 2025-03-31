from datetime import date
from django.db.models import Sum
from clientes.models import Cliente
from proyectos.models import Proyecto, Tarea, Responsable
from presupuestos.models import Presupuesto, Pago

def dashboard_callback(request, context):
    hoy = date.today()

    total_clientes = Cliente.objects.count()
    total_proyectos = Proyecto.objects.count()
    proyectos_finalizados = Proyecto.objects.filter(estado="finalizado").count()

    total_tareas = Tarea.objects.count()
    tareas_pendientes = Tarea.objects.filter(estado="pendiente").count()
    tareas_en_progreso = Tarea.objects.filter(estado="en_progreso").count()
    tareas_completadas = Tarea.objects.filter(estado="completada").count()
    tareas_vencidas = Tarea.objects.filter(fecha_limite__lt=hoy).exclude(estado="completada").count()

    total_presupuestos = Presupuesto.objects.count()
    presupuestos_aceptados = Presupuesto.objects.filter(estado="aceptado").count()
    presupuestos_rechazados = Presupuesto.objects.filter(estado="rechazado").count()
    presupuestos_enviados = Presupuesto.objects.filter(estado="enviado").count()
    presupuestos_vencidos = Presupuesto.objects.filter(fecha_vencimiento__lt=hoy, estado="enviado").count()

    monto_presupuestado = Presupuesto.objects.aggregate(total=Sum("monto_total"))["total"] or 0
    monto_pagado = Pago.objects.aggregate(total=Sum("monto"))["total"] or 0

    responsables = Responsable.objects.count()

    context.update({
        "kpis": [
            {"title": "Clientes", "metric": total_clientes},
            {"title": "Proyectos", "metric": total_proyectos},
            {"title": "Proyectos finalizados", "metric": proyectos_finalizados},

            {"title": "Tareas pendientes", "metric": tareas_pendientes},
            {"title": "Tareas en progreso", "metric": tareas_en_progreso},
            {"title": "Tareas completadas", "metric": tareas_completadas},
            {"title": "Tareas vencidas", "metric": tareas_vencidas},

            {"title": "Presupuestos enviados", "metric": presupuestos_enviados},
            {"title": "Presupuestos aceptados", "metric": presupuestos_aceptados},
            {"title": "Presupuestos rechazados", "metric": presupuestos_rechazados},
            {"title": "Presupuestos vencidos", "metric": presupuestos_vencidos},

            {"title": "Monto presupuestado", "metric": f"${monto_presupuestado:,.2f}"},
            {"title": "Monto pagado", "metric": f"${monto_pagado:,.2f}"},

            {"title": "Responsables", "metric": responsables},
        ]
    })
    return context
