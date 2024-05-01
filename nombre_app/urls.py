# nombre_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('usuario/<int:id>/', views.detalle_usuario, name='detalle_usuario'),
]


