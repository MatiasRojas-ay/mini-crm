from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Presupuesto

def presupuesto_pdf(request, pk):
    presupuesto = Presupuesto.objects.get(pk=pk)
    html_string = render_to_string("presupuestos/presupuesto_pdf.html", {"presupuesto": presupuesto})

    pdf_file = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = f"inline; filename=presupuesto_{pk}.pdf"
    return response