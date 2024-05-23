from django.db import models
from estudiantes.models import Estudiante, Tesis

# Create your models here.
class AprobacionTesis(models.Model):
    tesis = models.ForeignKey(Tesis, verbose_name="Tesis", on_delete=models.CASCADE)
    docente = models.ForeignKey('auth.User', verbose_name="Docente", on_delete=models.CASCADE)
    aprobada = models.BooleanField(verbose_name="Aprobada", default=False)
    comentario = models.TextField(verbose_name="Comentario", blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Aprobación de Tesis'
        verbose_name_plural = 'Aprobaciones de Tesis'
    
    def __str__(self):
        return f"Aprobación de '{self.tesis}' por {self.docente}"

