from rest_framework import viewsets
from .models import Reporte
from .serializers import ReporteSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all().order_by('-fecha_creacion')
    serializer_class = ReporteSerializer