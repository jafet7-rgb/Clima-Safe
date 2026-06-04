from django.urls import path, include
from rest_framework.routers import DefaultRouter
# ESTA ES LA LÍNEA QUE DEBES CORREGIR:
from .views import ReporteViewSet

router = DefaultRouter()
router.register(r'reportes', ReporteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]