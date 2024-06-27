from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professor(User):
    numero_trabajador = models.IntegerField(9)


class Students(User):
    matricula = models.CharField(max_length=100)    



class Principal(User):
    numero_trabajador = models.IntegerField() 
    