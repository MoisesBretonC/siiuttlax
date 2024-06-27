from django.db import models

class Semester(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
# Create your models here.
