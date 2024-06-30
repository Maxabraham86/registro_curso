from django.core.management.base import BaseCommand
from main.services import *


class Command(BaseCommand):

    def handle (self, *args, **kwargs):
    
        #p= crear_profesor('13216426-5', 'Profesor', 'Salomon')
        #p= crear_profesor('5432198-7', 'Profesor', 'Strange')
        #cp=crear_profesor('5632456-k', 'Benny', 'Goodman')
        #a= crear_estudiante('18234678-0', 'Bart', 'Simpson', '2008-12-23')
        #c= crear_estudiante('19456987-0','Juan','Perez', '1998-03-24')
        #c=crear_curso('QLI', 'Quality Laws Improvemente',2,'5632456-k')
        ce=agregar_curso_a_estudiante('UDE', '19456987-0')
        #o=obtiene_estudiante("18234678-0")
        #ad=agregar_direccion('Pedro Montt',564,'Lejia','vi','19456987-0')
        #ap=agregar_profesor_a_curso('98765432-1', 'KL01')
        #o=obtiene_direccion('18234678-0')
        #l= listar_profesores('')
        # ce=agregar_curso_a_estudiante('QLI', '18234678-0')
        # ap=agregar_profesor_a_curso('5632456-k', 'QLI')
        #c=crear_curso('UDE' , 'Universal data entry', 4,'5632456-k')
        o=obtiene_profesor("98765432-1")
        ie= imprime_estudiante_curso('19456987-0')
        
        #print ( 'o')
        