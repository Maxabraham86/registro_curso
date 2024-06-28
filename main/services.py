from main.models import *
from datetime import date

def crear_curso(codigo, nombre,version, profesor ):
    curso = Curso(codigo=codigo, nombre=nombre, version=version, profesor = profesor)
    curso.save()    

def crear_estudiante(rut, nombre, apellido,fecha_nac):
    estudiante=Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=True, created=date.today(), updated=date.today())
    estudiante.save()


def crear_profesor(rut, nombre, apellido):
    profesor=Profesor(rut=rut, nombre=nombre, apellido=apellido, created=date.today(), updated=date.today())
    profesor.save()

# ● crear_curso 
# ● crear_profesor 
# ● crear_estudiante 
# ● crear_direccion 
# ● obtiene_estudiante 
# ● obtiene_profesor 
# ● obtiene_curso 
# ● agrega_profesor_a_curso 
# ● agrega_cursos_a_estudiante 
# ● imprime_estudiante_cursos 