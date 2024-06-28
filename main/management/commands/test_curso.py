from django.core.management.base import BaseCommand
from main.services import *


class Command(BaseCommand):

    def handle (self, *args, **kwargs):
    
        p= crear_profesor('13216426-5', 'Profesor', 'Salomon')
        c=crear_curso('KL01', 'introduccion al klingon',1, p)
        
        a= crear_estudiante('16216426-5', 'pepe', 'grillo', '2001-05-23')
        print ( 'curso')