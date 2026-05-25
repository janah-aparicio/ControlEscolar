from django import forms
from .models import Estudiante, Profesor, Carrera, Materia, Aula, Grupo, PeriodoSemestral, Horario, Calificacion

# Clase base para ponerle los estilos de Bootstrap a cualquier formulario de forma automática
class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

# 1. FORMULARIO AUTOMÁTICO DE PROFESORES
class ProfesorForm(BootstrapModelForm):
    class Meta:
        model = Profesor
        fields = ['nomina', 'nombre', 'apellidos', 'email']

# 2. FORMULARIO AUTOMÁTICO DE CARRERAS
class CarreraForm(BootstrapModelForm):
    class Meta:
        model = Carrera
        fields = ['clave', 'nombre']

# 3. FORMULARIO AUTOMÁTICO DE MATERIAS
class MateriaForm(BootstrapModelForm):
    class Meta:
        model = Materia
        fields = ['clave', 'nombre', 'creditos', 'carrera']

# 4. FORMULARIO AUTOMÁTICO DE AULAS
class AulaForm(BootstrapModelForm):
    class Meta:
        model = Aula
        fields = ['nombre', 'capacidad', 'ubicacion']

 # 5. FORMULARIO AUTOMÁTICO DE GRUPOS
class GrupoForm(BootstrapModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'materia', 'profesor', 'aula','periodo', 'horario']  # Si en tus modelos tienes el campo 'periodo'

# 6. FORMULARIO AUTOMÁTICO DE PERIODOS
class PeriodoSemestralForm(BootstrapModelForm):
    class Meta:
        model = PeriodoSemestral
        fields = ['nombre']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

# 7. FORMULARIO AUTOMÁTICO DE HORARIOS
class HorarioForm(BootstrapModelForm):
    class Meta:
        model = Horario
        fields = ['dia', 'hora_inicio', 'hora_fin']
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
        }

# 8. FORMULARIO AUTOMÁTICO DE CALIFICACIONES
class CalificacionForm(BootstrapModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'materia','grupo', 'nota','periodo'] # Ajusta 'materia' por 'grupo' o 'nota' por 'calificacion' según tus campos exactos de models.py