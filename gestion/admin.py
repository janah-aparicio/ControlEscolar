
from django.contrib import admin
from .models import (
    Carrera, Profesor, Estudiante, Materia, 
    Aula, PeriodoSemestral, Horario, Grupo, Calificacion
)

# Registramos cada una de las 9 entidades para que aparezcan en el panel de control
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Aula)
admin.site.register(PeriodoSemestral)
admin.site.register(Horario)
admin.site.register(Grupo)
admin.site.register(Calificacion)
# Register your models here.
