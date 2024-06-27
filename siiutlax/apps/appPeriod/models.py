from django.db import models

class Semester(models.Model):
    PERIODS = [
        ('enero - abril','enero - abril'),
        ('mayo - agosto','mayo - agosto' )
        ('septiembre - diciembre','septiembre - diciembre')
    ]
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
# Create your models here.
