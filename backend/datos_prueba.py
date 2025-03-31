import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_crm.settings")
django.setup()

from clientes.models import Cliente
from presupuestos.models import Presupuesto, Pago
from proyectos.models import Proyecto, Tarea, Responsable

# Limpiar base de datos (opcional, usar con cuidado)
Cliente.objects.all().delete()
Presupuesto.objects.all().delete()
Pago.objects.all().delete()
Proyecto.objects.all().delete()
Tarea.objects.all().delete()
Responsable.objects.all().delete()

print("Base de datos limpia. Cargando datos de prueba...")

# Crear responsables
responsables = []
for i in range(3):
    r = Responsable.objects.create(
        nombre=f"Responsable {i+1}",
        email=f"responsable{i+1}@mail.com"
    )
    responsables.append(r)

# Crear clientes
clientes = []
for i in range(5):
    c = Cliente.objects.create(
        nombre=f"Cliente {i+1}",
        email=f"cliente{i+1}@mail.com",
        telefono=f"+595 981 000{i}",
        empresa=f"Empresa {i+1}",
        notas="Cliente creado con datos de prueba."
    )
    clientes.append(c)

# Crear presupuestos y proyectos
estados_presupuesto = ['enviado', 'aceptado', 'rechazado']
estados_proyecto = ['pendiente', 'en_progreso', 'finalizado']
proyectos = []

for cliente in clientes:
    presupuesto = Presupuesto.objects.create(
        cliente=cliente,
        monto_total=random.randint(300, 2000),
        estado=random.choice(estados_presupuesto),
        fecha_vencimiento=date.today() + timedelta(days=random.randint(10, 30))
    )

    proyecto = Proyecto.objects.create(
        cliente=cliente,
        nombre=f"Proyecto de {cliente.nombre}",
        descripcion="Proyecto generado automáticamente",
        estado=random.choice(estados_proyecto),
        fecha_inicio=date.today() - timedelta(days=random.randint(10, 50)),
        fecha_fin=None,
        presupuesto=presupuesto
    )
    proyectos.append(proyecto)

    # Crear pagos si el presupuesto fue aceptado
    if presupuesto.estado == 'aceptado':
        Pago.objects.create(
            presupuesto=presupuesto,
            monto=presupuesto.monto_total,
            fecha=date.today(),
            metodo=random.choice(["Transferencia", "Efectivo", "Tarjeta"])
        )

# Crear tareas para cada proyecto
for proyecto in proyectos:
    for i in range(random.randint(2, 4)):
        Tarea.objects.create(
            proyecto=proyecto,
            titulo=f"Tarea {i+1} - {proyecto.nombre}",
            descripcion="Tarea de prueba generada automáticamente.",
            prioridad=random.choice(['baja', 'media', 'alta']),
            estado=random.choice(['pendiente', 'en_progreso', 'completada']),
            fecha_limite=date.today() + timedelta(days=random.randint(1, 15)),
            responsable=random.choice(responsables)
        )

print("✔ Datos de prueba generados exitosamente.")