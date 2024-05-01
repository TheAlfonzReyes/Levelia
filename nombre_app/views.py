from django.shortcuts import render
from .models import Usuario, Proyecto

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()  # Obtiene todos los proyectos
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

def detalle_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)  # Obtiene el usuario por ID
    return render(request, 'detalle_usuario.html', {'usuario': usuario})


# Create your views here.
