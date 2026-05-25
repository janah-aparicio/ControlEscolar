"""
URL configuration for ControlEscolar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestion import views  # Importamos las vistas de tu app gestion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),  # <-- Agrega esta
    path('estudiantes/nuevo/', views.crear_estudiante, name='crear_estudiante'), # <-- Nueva línea
    path('profesores/', views.lista_profesores, name='lista_profesores'),  # <-- Nueva
    path('profesores/nuevo/', views.crear_profesor, name='crear_profesor'),
    path('carreras/', views.lista_carreras, name='lista_carreras'),
    
           
    path('grupos/', views.lista_grupos, name='lista_grupos'),          # <-- Nueva
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('carreras/nueva/', views.crear_carrera, name='crear_carrera'),
    
    
    path('grupos/nuevo/', views.alta_grupo, name='crear_grupo'),
    path('periodos/nuevo/', views.crear_periodo, name='crear_periodo'),
    path('horarios/nuevo/', views.crear_horario, name='crear_horario'),
    path('calificaciones/', views.lista_calificaciones, name='lista_calificaciones'),
    path('calificaciones/nueva/', views.crear_calificacion, name='crear_calificacion'),
    path('reporte/', views.reporte_general, name='reporte_general'),
    # Rutas para el control de Estudiantes (Editar y Eliminar)
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    # Rutas para la gestión de Grupos (Editar y Eliminar)
    path('grupos/editar/<int:id>/', views.editar_grupo, name='editar_grupo'),
    path('grupos/eliminar/<int:id>/', views.eliminar_grupo, name='eliminar_grupo'),
    path('calificaciones/editar/<int:id>/', views.editar_calificacion, name='editar_calificacion'),
    path('calificaciones/eliminar/<int:id>/', views.eliminar_calificacion, name='eliminar_calificacion'),
    path('profesores/editar/<int:id>/', views.editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:id>/', views.eliminar_profesor, name='eliminar_profesor'),
    path('carreras/editar/<int:id>/', views.editar_carrera, name='editar_carrera'),
    path('carreras/eliminar/<int:id>/', views.eliminar_carrera, name='eliminar_carrera'),
    
    # Módulo Materias 
    path('materias/', views.lista_materias, name='lista_materias'),
    path('materias/nueva/', views.registrar_materia, name='registrar_materia'),  # Apunta a la nueva función
    path('materias/editar/<int:id>/', views.editar_materia, name='editar_materia'),
    path('materias/eliminar/<int:id>/', views.eliminar_materia, name='eliminar_materia'),


    path('aulas/', views.lista_aulas, name='lista_aulas'),
    path('aulas/nueva/', views.registrar_aula, name='registrar_aula'),
    path('aulas/editar/<int:id>/', views.editar_aula, name='editar_aula'),
    path('aulas/eliminar/<int:id>/', views.eliminar_aula, name='eliminar_aula'),
]



