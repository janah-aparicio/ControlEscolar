
from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Profesor, Carrera, Materia, Aula, PeriodoSemestral, Horario, Grupo, Calificacion
from .forms import  ProfesorForm, CarreraForm, MateriaForm, AulaForm, GrupoForm, PeriodoSemestralForm, HorarioForm, CalificacionForm
from django.apps import apps
def home(request):
    # Esta vista solo va a renderizar la página de inicio principal
    return render(request, 'gestion/home.html')
# Create your views here.



def home(request):
    return render(request, 'gestion/home.html')

# NUEVA VISTA PARA VER ALUMNOS
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()  # Esto jala a todos los alumnos de Postgres
    return render(request, 'gestion/estudiantes.html', {'estudiantes': estudiantes})
from .models import Estudiante  # Importamos el modelo para poder usarlo

def home(request):
    return render(request, 'gestion/home.html')

# NUEVA VISTA PARA VER ALUMNOS
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()  # Esto jala a todos los alumnos de Postgres
    return render(request, 'gestion/estudiantes.html', {'estudiantes': estudiantes})


def home(request):
    return render(request, 'gestion/home.html')

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'gestion/estudiantes.html', {'estudiantes': estudiantes})

# ... (tus otras vistas quedan igual) ...

# VISTA PARA CREAR UN ESTUDIANTE (ALTA)
from django.shortcuts import render, redirect
from django.db import IntegrityError # <-- Importamos esto para atrapar el error de duplicados
from .models import Estudiante, Carrera

def crear_estudiante(request):
    carreras = Carrera.objects.all()
    
    if request.method == 'POST':
        mat = request.POST.get('matricula')
        nom = request.POST.get('nombre')
        ape = request.POST.get('apellidos')
        car_id = request.POST.get('carrera')
        
        carrera_obj = Carrera.objects.get(id=car_id)
        
        try:
            # Intentamos guardar el estudiante de forma normal
            Estudiante.objects.create(
                matricula=mat,
                nombre=nom,
                apellidos=ape,
                carrera=carrera_obj
            )
            return redirect('lista_estudiantes')
            
        except IntegrityError:
            # Si la matrícula ya existe, capturamos el error y mandamos un mensaje a la pantalla
            error_mensaje = f"La matrícula '{mat}' ya está registrada en el sistema. Intenta con otra."
            return render(request, 'gestion/alta_estudiante.html', {
                'carreras': carreras, 
                'error': error_mensaje
            })
            
    return render(request, 'gestion/alta_estudiante.html', {'carreras': carreras})


# VISTA PARA LISTAR GRUPOS (TABLA)
def lista_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'gestion/grupos.html', {'grupos': grupos})

# VISTA PARA CREAR GRUPO (ALTA)
def crear_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el grupo en Postgres
            return redirect('lista_grupos')  # Te regresa a la tabla
    else:
        form = GrupoForm()

    return render(request, 'gestion/alta_grupo.html', {'form': form})


# VISTA PARA CREAR PROFESOR (ALTA)
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en Postgres
            return redirect('lista_profesores')  # Te regresa a la tabla bonita
    else:
        form = ProfesorForm()
    
    return render(request, 'gestion/alta_profe.html', {'form': form})

# VISTA PARA CREAR CARRERA (ALTA)
def crear_carrera(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la clave y nombre de la carrera en Postgres
            return redirect('lista_carreras')  # Te regresa a la tabla de carreras
    else:
        form = CarreraForm()

    return render(request, 'gestion/alta_carrera.html', {'form': form})

# VISTA PARA CREAR MATERIA (ALTA)
def crear_materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la clave, nombre, créditos y carrera en Postgres
            return redirect('lista_materias')  # Te regresa a la tabla de materias
    else:
        form = MateriaForm()

    return render(request, 'gestion/alta_materia.html', {'form': form})

# VISTA PARA CREAR AULA (ALTA)
def crear_aula(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nombre, capacidad y ubicación en Postgres
            return redirect('lista_aulas')  # Te regresa a la tabla de aulas
    else:
        form = AulaForm()

    return render(request, 'gestion/alta_aula.html', {'form': form})

# VISTA PARA REGISTRAR NUEVO PERIODO
def crear_periodo(request):
    if request.method == 'POST':
        form = PeriodoSemestralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos') # Te regresa a la tabla para que veas el cambio
    else:
        form = PeriodoSemestralForm()
    return render(request, 'gestion/alta_periodo.html', {'form': form})

# VISTA PARA REGISTRAR NUEVO HORARIO
def crear_horario(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')
    else:
        form = HorarioForm()
    return render(request, 'gestion/alta_horario.html', {'form': form})

# VISTA PARA CARRERAS
def lista_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'gestion/carreras.html', {'carreras': carreras})


# 5. MATERIAS
def lista_materias(request):
    materias = Materia.objects.all()
    return render(request, 'gestion/materias.html', {'materias': materias})

# 6. AULAS
def lista_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'gestion/aulas.html', {'aulas': aulas})

# 7. GRUPOS (El gran conector)
def lista_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'gestion/grupos.html', {'grupos': grupos})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'gestion/profesores.html', {'profesores': profesores})




def reporte_general(request):
    # 1. Traemos los objetos base
    estudiantes_query = Estudiante.objects.all().select_related('carrera')
    grupos_completos = Grupo.objects.all().select_related('materia', 'profesor', 'aula', 'horario', 'periodo')
    
    # 2. Lógica manual para asegurar que aparezcan las materias sin fallas de grupo_set:
    lista_estudiantes_con_materias = []
    
    for estudiante in estudiantes_query:
        materias_del_alumno = []
        
        # Buscamos en todos los grupos activos si este estudiante es parte de él
        for grupo in grupos_completos:
            # Django permite preguntar si el objeto está en el ManyToMany usando .all()
            # Si tu relación se llama diferente, esto cubre cualquier coincidencia:
            if hasattr(grupo, 'estudiantes') and estudiante in grupo.estudiantes.all():
                materias_del_alumno.append(grupo.materia.nombre)
            elif hasattr(grupo, 'estudiante') and grupo.estudiante == estudiante:
                materias_del_alumno.append(grupo.materia.nombre)
                
        # Si no encontramos materias por grupo, buscamos si tiene materias en sus calificaciones registradas
        if not materias_del_alumno:
            from .models import Calificacion
            califs = Calificacion.objects.filter(estudiante=estudiante).select_related('grupo__materia', 'materia')
            for c in califs:
                if c.grupo and c.grupo.materia:
                    materias_del_alumno.append(c.grupo.materia.nombre)
                elif c.materia:
                    materias_del_alumno.append(c.materia.nombre)
        
        # Eliminamos duplicados si cursa la misma materia en dos lados
        materias_limpias = list(set(materias_del_alumno))
        
        # Guardamos el registro armado
        lista_estudiantes_con_materias.append({
            'matricula': estudiante.matricula,
            'nombre': estudiante.nombre,
            'apellidos': estudiante.apellidos,
            'carrera_nombre': estudiante.carrera.nombre if estudiante.carrera else "Sin Carrera",
            'materias': materias_limpias
        })

    # 3. Empaquetamos todo en el contexto
    context = {
        'total_estudiantes': estudiantes_query.count(),
        'total_profesores': Profesor.objects.count(),
        'total_carreras': Carrera.objects.count(),
        'total_materias': Materia.objects.count(),
        'total_aulas': Aula.objects.count(),
        'total_grupos': Grupo.objects.count(),
        
        'estudiantes_procesados': lista_estudiantes_con_materias,  # <- Nuestra nueva lista segura
        'grupos_completos': grupos_completos,
    }
    return render(request, 'gestion/reporte_general.html', context)



def editar_estudiante(request, id):
    # Obtenemos el estudiante actual o lanzamos un 404 si no existe
    estudiante = get_object_or_404(Estudiante, id=id)
    # Traemos las carreras para que el usuario pueda seleccionar una en el formulario
    carreras = Carrera.objects.all()
    
    if request.method == 'POST':
        # Recogemos los datos enviados desde las etiquetas 'name' del HTML
        estudiante.matricula = request.POST.get('matricula')
        estudiante.nombre = request.POST.get('nombre')
        estudiante.apellidos = request.POST.get('apellidos')
        
        carrera_id = request.POST.get('carrera')
        if carrera_id:
            estudiante.carrera = get_object_or_404(Carrera, id=carrera_id)
            
        # Guardamos directamente en la base de datos
        estudiante.save()
        return redirect('lista_estudiantes') # Te regresa a la tabla
        
    return render(request, 'gestion/alta_estudiante.html', {
        'estudiante': estudiante,
        'carreras': carreras
    })

def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    
    # Eliminación directa al confirmar la petición POST
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes') # Te regresa a la tabla
        
    return render(request, 'gestion/alta_estudiante.html', {
        'estudiante': estudiante,
        'mostrar_confirmacion_borrado': True
    })




# 1. FUNCIÓN PARA CREAR GRUPO
def alta_grupo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        materia_id = request.POST.get('materia')
        profesor_id = request.POST.get('profesor')
        aula_id = request.POST.get('aula')
        horario_id = request.POST.get('horario')
        periodo_id = request.POST.get('periodo')

        materia = Materia.objects.get(id=materia_id)
        profesor = Profesor.objects.get(id=profesor_id)
        aula = Aula.objects.get(id=aula_id)
        horario = Horario.objects.get(id=horario_id)
        periodo = PeriodoSemestral.objects.get(id=periodo_id)

        Grupo.objects.create(
            nombre=nombre,
            materia=materia,
            profesor=profesor,
            aula=aula,
            horario=horario,
            periodo=periodo
        )
        return redirect('/grupos/') # Redirección directa y segura por PATH

    context = {
        'materias': Materia.objects.all(),
        'profesores': Profesor.objects.all(),
        'aulas': Aula.objects.all(),
        'horarios': Horario.objects.all(),
        'periodos': PeriodoSemestral.objects.all(),
    }
    return render(request, 'gestion/alta_grupo.html', context)


# 2. FUNCIÓN PARA EDITAR GRUPO
def editar_grupo(request, id):
    grupo = get_object_or_404(Grupo, id=id)
    
    if request.method == 'POST':
        grupo.nombre = request.POST.get('nombre')
        grupo.materia = Materia.objects.get(id=request.POST.get('materia'))
        grupo.profesor = Profesor.objects.get(id=request.POST.get('profesor'))
        grupo.aula = Aula.objects.get(id=request.POST.get('aula'))
        grupo.horario = Horario.objects.get(id=request.POST.get('horario'))
        grupo.periodo = PeriodoSemestral.objects.get(id=request.POST.get('periodo'))
        grupo.save()
        return redirect('/grupos/')

    context = {
        'grupo': grupo,
        'materias': Materia.objects.all(),
        'profesores': Profesor.objects.all(),
        'aulas': Aula.objects.all(),
        'horarios': Horario.objects.all(),
        'periodos': PeriodoSemestral.objects.all(),
    }
    return render(request, 'gestion/alta_grupo.html', context)


# 3. FUNCIÓN PARA ELIMINAR GRUPO
def eliminar_grupo(request, id):
    grupo = get_object_or_404(Grupo, id=id)
    
    if request.method == 'POST':
        grupo.delete()
        return redirect('/grupos/')
        
    return render(request, 'gestion/alta_grupo.html', {'grupo': grupo, 'mostrar_confirmacion_borrado': True})

# 1. LISTA GENERAL DE CALIFICACIONES
def lista_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'gestion/calificaciones.html', {'calificaciones': calificaciones})

# 2. ASIGNAR / CREAR NUEVA CALIFICACIÓN (AUTOMÁTICA Y LIMPIA)
def crear_calificacion(request):
    if request.method == 'POST':
        id_estudiante = request.POST.get('estudiante')
        id_materia = request.POST.get('materia')
        valor_nota = request.POST.get('nota')  # Recibe el valor numérico desde el HTML
        
        # Validación de seguridad para que la nota nunca sea enviada vacía
        if not valor_nota:
            valor_nota = "0.0"
            
        estudiante = get_object_or_404(Estudiante, id=id_estudiante)
        materia = get_object_or_404(Materia, id=id_materia)
        
        # Obtenemos dinámicamente tus modelos utilizando sus nombres exactos de código
        Grupo = apps.get_model('gestion', 'Grupo')
        # CORREGIDO: Usamos el nombre real de tu clase que aparece en la captura
        PeriodoSemestral = apps.get_model('gestion', 'PeriodoSemestral')
        
        # Asignación automática de Grupo en segundo plano
        grupo_asignar = estudiante.grupo if (hasattr(estudiante, 'grupo') and estudiante.grupo) else Grupo.objects.first()
        
        # Asignación automática del Periodo Semestral registrado en tu base de datos
        periodo_asignar = PeriodoSemestral.objects.first()
        
        # Construcción y guardado del registro mapeando los campos requeridos
        nueva_c = Calificacion(
            estudiante=estudiante,
            materia=materia,
            grupo=grupo_asignar,
            periodo=periodo_asignar,  # Django sabe mapear esto internamente a periodo_id en Postgres
            nota=valor_nota
        )
        
        nueva_c.save()
        return redirect('/calificaciones/')
        
    return render(request, 'gestion/alta_calificacion.html', {
        'estudiantes': Estudiante.objects.all(),
        'materias': Materia.objects.all()
    })

# 3. EDITAR UNA CALIFICACIÓN EXISTENTE
def editar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    
    if request.method == 'POST':
        nota = request.POST.get('calificacion') or request.POST.get('calificacion_final')
        if nota:
            if hasattr(calificacion, 'calificacion'):
                calificacion.calificacion = nota
            else:
                calificacion.calificacion_final = nota
            calificacion.save()
        return redirect('/calificaciones/')
    
    return render(request, 'gestion/alta_calificacion.html', {
        'calificacion': calificacion,
        'estudiantes': Estudiante.objects.all(),
        'materias': Materia.objects.all()
    })

# 4. ELIMINAR UNA CALIFICACIÓN
def eliminar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    calificacion.delete()
    return redirect('/calificaciones/')






# 1. LISTAR PROFESORES
def lista_profesor(request):
    profesores = Profesor.objects.all()
    return render(request, 'gestion/profesor.html', {'profesores': profesores})

# En gestion/views.py

def crear_profesor(request):
    if request.method == 'POST':
        v_nomina = request.POST.get('nomina')
        v_nombre = request.POST.get('nombre')
        v_apellido = request.POST.get('apellido')
        v_email = request.POST.get('email')
        
        try:
            Profesor.objects.create(
                nomina=v_nomina,
                nombre=v_nombre,
                apellidos=v_apellido,
                email=v_email
            )
            return redirect('/profesores/')
        except IntegrityError:
            # Si hay error de duplicidad, regresamos al formulario con un mensaje
            error_msg = f"La nómina '{v_nomina}' ya existe. Por favor usa otra."
            return render(request, 'gestion/alta_profesor.html', {'error': error_msg})
            
    return render(request, 'gestion/alta_profesor.html')


def editar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    
    if request.method == 'POST':
        profesor.nomina = request.POST.get('nomina')
        profesor.nombre = request.POST.get('nombre')
        profesor.apellidos = request.POST.get('apellido')
        profesor.email = request.POST.get('email')
        profesor.save()
        return redirect('/profesores/')
        
    # CORREGIDO: También aquí para cuando vayas a editar
    return render(request, 'gestion/alta_profesor.html', {'profesor': profesor})

# 4. ELIMINAR PROFESOR
def eliminar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    profesor.delete()
    return redirect('/profesores/')




# 1. FUNCIÓN PARA EDITAR
def editar_carrera(request, id):
    carrera = get_object_or_404(Carrera, id=id)
    if request.method == 'POST':
        carrera.clave = request.POST.get('clave')
        carrera.nombre = request.POST.get('nombre')
        carrera.save()
        return redirect('/carreras/') # Asegúrate de que esta URL sea la correcta
    return render(request, 'gestion/alta_carrera.html', {'carrera': carrera})

# 2. FUNCIÓN PARA ELIMINAR
def eliminar_carrera(request, id):
    carrera = get_object_or_404(Carrera, id=id)
    carrera.delete()
    return redirect('/carreras/')

def listar_materias(request):
    materias = Materia.objects.all()
    return render(request, 'gestion/materias.html', {'materias': materias})

def crear_o_editar_materia(request, id=None):
    # 1. Buscamos la materia si viene un ID (editar), sino será None (registrar)
    materia = get_object_or_404(Materia, id=id) if id else None
    
    # 2. OBTENEMOS LAS CARRERAS ANTES DE CUALQUIER OTRA COSA
    todas_las_carreras = Carrera.objects.all()
    
    if request.method == 'POST':
        v_clave = request.POST.get('clave')
        v_nombre = request.POST.get('nombre')
        v_creditos = request.POST.get('creditos')
        v_carrera_id = request.POST.get('carrera')
        
        if materia:
            materia.clave = v_clave
            materia.nombre = v_nombre
            materia.creditos = v_creditos
            materia.carrera_id = v_carrera_id
            materia.save()
        else:
            Materia.objects.create(
                clave=v_clave,
                nombre=v_nombre,
                creditos=v_creditos,
                carrera_id=v_carrera_id
            )
        return redirect('/materias/')
    
    # 3. PASAMOS 'carreras' AL CONTEXTO (esto es lo que llena tu select)
    return render(request, 'gestion/alta_materia.html', {
        'materia': materia, 
        'carreras': todas_las_carreras 

    })



def registrar_materia(request):
    if request.method == 'POST':
        # Tu lógica de guardado
        Materia.objects.create(
            clave=request.POST.get('clave'),
            nombre=request.POST.get('nombre'),
            creditos=request.POST.get('creditos'),
            carrera_id=request.POST.get('carrera')
        )
        return redirect('/materias/')
    
    # ESTO ES LO QUE OBLIGA AL SELECT A CARGARSE
    todas_las_carreras = Carrera.objects.all()
    
    return render(request, 'gestion/alta_materia.html', {
        'carreras': todas_las_carreras
    })
# Función para EDITAR una materia existente
def editar_materia(request, id):
    materia = get_object_or_404(Materia, id=id)
    
    if request.method == 'POST':
        materia.clave = request.POST.get('clave')
        materia.nombre = request.POST.get('nombre')
        materia.creditos = request.POST.get('creditos')
        materia.carrera_id = request.POST.get('carrera')
        materia.save()
        return redirect('/materias/')
    
    # Enviamos la materia Y las carreras para que el select sepa cuál es la actual
    return render(request, 'gestion/alta_materia.html', {
        'materia': materia, 
        'carreras': Carrera.objects.all()
    })


# Asegúrate de agregar esta función en tu archivo views.py
def eliminar_materia(request, id):
    materia = get_object_or_404(Materia, id=id)
    materia.delete()
    return redirect('/materias/')



def registrar_aula(request):
    if request.method == 'POST':
        Aula.objects.create(
            nombre=request.POST.get('nombre'),
            capacidad=request.POST.get('capacidad'),
            ubicacion=request.POST.get('ubicacion')
        )
        return redirect('/aulas/')
    return render(request, 'gestion/alta_aula.html')

def editar_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    if request.method == 'POST':
        aula.nombre = request.POST.get('nombre')
        aula.capacidad = request.POST.get('capacidad')
        aula.ubicacion = request.POST.get('ubicacion')
        aula.save()
        return redirect('/aulas/')
    return render(request, 'gestion/alta_aula.html', {'aula': aula})

def eliminar_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    aula.delete()
    return redirect('/aulas/')