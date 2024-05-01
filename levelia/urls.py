# levelia/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nombre_app.urls')),  # Ruta raíz redirigida a las URLs de tu aplicación
]
