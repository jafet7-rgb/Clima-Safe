from django.contrib import admin
from django.urls import path, include
from django.conf import settings           # <-- REVISA QUE ESTA LÍNEA ESTÉ AQUÍ
from django.conf.urls.static import static # <-- Y ESTA TAMBIÉN

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reportes.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)