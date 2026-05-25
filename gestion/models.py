

from django.db import models

# 1. CARRERA
class Carrera(models.Model):
    clave = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 2. PROFESOR
class Profesor(models.Model):
    nomina = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

# 3. ESTUDIANTE
class Estudiante(models.Model):
    matricula = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

# 4. MATERIA
class Materia(models.Model):
    clave = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# 5. AULA
class Aula(models.Model):
    nombre = models.CharField(max_length=20) 
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100) 

    def __str__(self):
        return self.nombre

# 6. PERIODO SEMESTRAL
class PeriodoSemestral(models.Model):
    nombre = models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre

# 7. HORARIO
class Horario(models.Model):
    dia = models.CharField(max_length=20) 
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.dia} ({self.hora_inicio} - {self.hora_fin})"

# 8. GRUPO
class Grupo(models.Model):
    nombre = models.CharField(max_length=10) 
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    periodo = models.ForeignKey(PeriodoSemestral, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, blank=True)

    def __str__(self):
        return f"Grupo {self.nombre} - {self.materia.nombre}"

# 9. CALIFICACIÓN
class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    periodo = models.ForeignKey(PeriodoSemestral, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2) 

    def __str__(self):
        return f"{self.estudiante} - {self.materia.nombre}: {self.nota}"