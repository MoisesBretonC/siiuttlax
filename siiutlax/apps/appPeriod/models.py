from django.db import models

class Period(models.Model):
    MONTHS_PERIOD = [
        ('enero - abril', 'enero - abril'),
        ('mayo - agosto', 'mayo - agosto'),
        ('septiembre - diciembre', 'septiembre - diciembre'),
    ]
    period = models.CharField(max_length=25, choices=MONTHS_PERIOD,verbose_name='Periodo')
    year = models.IntegerField(verbose_name='Año',default=2024)
    cycle = models.CharField(max_length=10, verbose_name='Ciclo', default='2024-2025')
    is_active= models.BooleanField(verbose_name='Activo', default=False)
    
    def __str__(self):
        return f'{self.period}{self.year}'
    
    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Cuatrimestre'
        ordering=['id']


class Semester(models.Model):
    semester = models.CharField(max_length=2, verbose_name="Cuatrimestre")
    semester_name = models.CharField(max_length=10,verbose_name="Cuatrimestre en Letra")