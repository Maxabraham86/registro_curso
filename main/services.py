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
        updated=date.today()
        )
    estudiante.save()


def crear_profesor(rut, nombre, apellido):
    profesor=Profesor(rut=rut, 
                    nombre=nombre,
                    apellido=apellido,
                    created=date.today(null=True),
                    updated=date.today(null=True)
                    )
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

def agregar_direccion(calle,numero,comuna,region,estudiante_rut):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    d= Direccion(calle=calle, numero=numero,comuna=comuna, region=region, estudiante=estudiante)
    d.save()
    
    
def obtiene_estudiante(estudiante_rut):
    e=Estudiante.objects.get(rut=estudiante_rut)
    print(e)
    
def obtiene_profesor(profesor_rut):
    
        p=Profesor.objects.get(rut=profesor_rut)
    
        print(p)
    
def obtiene_direccion(estudiante_rut):
    estudiante=Estudiante.objects.get(rut=estudiante_rut)
    
    direccion=Direccion.objects.filter(estudiante=estudiante).first()
    if direccion:
        print(direccion)
    else:
        print ('no hay direccion para el estudiante con Rut {estudiante_rut}')

def listar_profesores(profesor_rut):
    p=Profesor.objects.all()
    print(p)

def imprime_estudiante_curso(estudiante_rut):
    try:
        estudiante = Estudiante.objects.get(rut= estudiante_rut)
        cursos= estudiante.cursos.all()
        print(f'Estudiante:{estudiante.nombre} {estudiante.apellido} (Rut {estudiante_rut})')
        if cursos:
            for curso in cursos:
                print(f'  - {curso.nombre} (codigo: {curso.codigo}, Version: { curso.version})')
        else:
                print ('No está inscrito en ningun curso.')
    except Estudiante.DoesNotExist:
        print (f'No se encontró un estudiante con el Rut {estudiante_rut}')
                
                
    
# ● imprime_estudiante_cursos 