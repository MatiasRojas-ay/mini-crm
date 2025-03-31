from django.urls import path
from .views import presupuesto_pdf


urlpatterns = [
    path('<int:pk>/pdf/', presupuesto_pdf, name='presupuesto_pdf'),
]