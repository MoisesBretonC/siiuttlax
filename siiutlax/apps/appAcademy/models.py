from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=15)
    description = models.TextField()
    

class Professor(User):
    numero_trabajador = models.IntegerField(9)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)


class Students(User):
    matricula = models.CharField(max_length=12)    


class Principal(User):
    numero_trabajador = models.IntegerField() 
    