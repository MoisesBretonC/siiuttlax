from django.contrib import admin
<<<<<<< HEAD
from .models import Period, Semester
=======
from .models import Period,Semester

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display=['year', 'period', 'cycle','is_active']
    list_editable=['is_active']
    
@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display=['semester_name']

>>>>>>> 2b60723b5be0a81f3b9312cb2559db2e4e204932

# Register your models here.

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display=['year', 'period', 'cicle','is_active']
    list_editable=['is_active']
    
@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display=['semester_name']

