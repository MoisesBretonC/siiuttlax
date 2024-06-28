from django.db import models

# Create your models here.

class Career(models.Model):
    LEVELS = (
        ('TSU', 'Tecnica Superior Universitario'),
        ('Ing', 'Ingenieria'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestria'),

    )

    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    level = models.CharField(max_length=3, choices=LEVELS)
    year_plan= models.CharField(max_length=4)
    status = models.BooleanField(default=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.IntegerField() #ForeignKey a semester
    total_hours = models.IntegerField()
    weekly_hours = models.IntegerField()
    file = models.CharField(max_length=100)
    