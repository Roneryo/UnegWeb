from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Estudiante(models.Model):
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	edad=models.IntegerField()
	
