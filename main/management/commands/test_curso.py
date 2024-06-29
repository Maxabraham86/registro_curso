from django.core.management.base import BaseCommand
from main.services import *


class Command(BaseCommand):

    def handle (self, *args, **kwargs):
    
        #p= crear_profesor('13216426-5', 'Profesor', 'Salomon')
        p= crear_profesor('65432198-7', 'Profesor', 'Jones')
        #a= crear_estudiante('16216426-5', 'pepe', 'grillo', '2001-05-23')
        #c=crear_curso('KL01', 'introduccion al klingon',1,'13216426-5')
        #ce=agregar_curso_a_estudiante('KL01', '16216426-5')
        
        #cp=crear_profesor('98765432-1', 'Avelardo', 'Valenzuela')
        
        #ap=agregar_profesor_a_curso('98765432-1', 'KL01')
        print ( 'curso')