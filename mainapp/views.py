from django.shortcuts import render
from .models import Estudiante, Tesis

def index(request):
    estudiantes = Estudiante.objects.all()
    tesis_aprobadas = Tesis.objects.filter(aprobada=True)
    tesis_pendientes = Tesis.objects.filter(aprobada=False)
    
    return render(request, 'tu_app/index.html', {
        'titulo': 'Página de inicio',
        'estudiantes': estudiantes,
        'tesis_aprobadas': tesis_aprobadas,
        'tesis_pendientes': tesis_pendientes
    })
