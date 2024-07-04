
from django.db import models
from apps.appAcademy.models import Professor
from apps.appPeriod.models import Semester
# Create your models here.


class Career(models.Model):
    LEVELS = (
        ('TSU', 'Tecnica Superior Universitario'),
        ('Ing', 'Ingenieria'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestria'),
    )
    director = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Director"
    )
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    level = models.CharField(max_length=3, choices=LEVELS)
    year_plan = models.CharField(max_length=4)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.level}-{self.short_name}"
   

class Subject(models.Model):
    name = models.CharField(max_length=100)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        default=1)
    total_hours = models.IntegerField()
    weekly_hours = models.IntegerField()
    file = models.CharField(max_length=100)

# haciendo los metas    

class Meta:
    verbose_name = 'carrera'
    verbose_name_plural = 'carreras'