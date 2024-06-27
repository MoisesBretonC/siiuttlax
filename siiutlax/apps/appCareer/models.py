from django.db import models

# Create your models here.

class Career(models.Model):
    name = models.CharField(max_length=100)
    level = models.TextField()
    shorcuts = models.CharField(max_length=100)
    status = models.TextField()
    plan = models.DateField(auto_now_add=True)
    director = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name