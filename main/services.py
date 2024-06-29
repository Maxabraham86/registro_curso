from main.models import *
from datetime import date

def crear_curso(codigo, nombre,version, profesor_rut ):
    p= Profesor.objects.get(rut=profesor_rut)
    curso = Curso(codigo=codigo, nombre=nombre, version=version, profesor = p)
    curso.save()    

def crear_estudiante(rut, nombre, apellido,fecha_nac):
    estudiante=Estudiante(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nac=fecha_nac,
        activo=True,
        created=date.today(),
        updated=date.today())
    estudiante.save()


def crear_profesor(rut, nombre, apellido):
    profesor=Profesor(rut=rut, nombre=nombre, apellido=apellido, created=date.today(), updated=date.today())
    profesor.save()


def agregar_curso_a_estudiante(curso_codigo, estudiante_rut):
    
    #1. recuperamos el curso y el estudiante que deseamos recuperar
    c= Curso.objects.get(codigo=curso_codigo)
    e = Estudiante.objects.get(rut= estudiante_rut)
    #2 Vincular ambas entidades
    c.estudiantes.add(e)



def crear_profesor(rut, nombre, apellido):
    p=Profesor(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=True)
        # created=date.today(),
        # updated=date.today())
    p.save()
def agregar_profesor_a_curso(profesor_rut, curso_codigo):
    p=Profesor.objects.get(rut=profesor_rut)
    c=Curso.objects.get(codigo=curso_codigo)
    c.profesor=p
    c.save()



# ● crear_direccion 

# ● obtiene_estudiante 
# ● obtiene_profesor 
# ● obtiene_curso 
# ● agrega_profesor_a_curso 
# ● agrega_cursos_a_estudiante 
# ● imprime_estudiante_cursos 