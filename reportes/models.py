from django.db import models

class Reporte(models.Model):
    # Opciones exactas de tu select en HTML
    OPCIONES_INCIDENTE = [
        ('inundacion', 'Inundación'),
        ('derrumbe', 'Derrumbe / Deslave'),
        ('arbol', 'Árbol Caído'),
    ]

    tipo_incidente = models.CharField(max_length=20, choices=OPCIONES_INCIDENTE)
    descripcion = models.TextField()
    evidencia = models.ImageField(upload_to='evidencias/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Coordenadas preparadas para cuando integremos el mapa
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.get_tipo_incidente_display()} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"