from django.db import models

# Create your models here.

class Estudiante(models.Model):
    rut=models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo= models.BooleanField(default= False)
    created = models.DateField(auto_now_add=True)
    updated= models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.nombre}  {self.apellido}'
    

class Direccion(models.Model):
    regiones= (('iii','Atacama'),('v','Valparaiso'),('ix', 'Araucania'),('vi', "O'Higgins"))
    calle= models.CharField(max_length=50)
    numero= models.CharField(max_length=10)
    comuna= models.CharField(max_length=50)
    region= models.CharField(max_length=50, choices=regiones)
    estudiante= models.OneToOneField(Estudiante, related_name='direccion', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.calle}  {self.comuna}'

class Profesor(models.Model):
    rut=models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated= models.DateField(auto_now=True)


class Curso(models.Model):
    codigo=models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    version=models.IntegerField()
    profesor= models.ForeignKey(Profesor, related_name='cursos', on_delete=models.CASCADE)
    estudiantes =models.ManyToManyField(Estudiante, related_name='cursos')
    
    