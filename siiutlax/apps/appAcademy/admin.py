from django.contrib import admin

from .models import Category,Professor, Student


# Register your models here.

admin.site.register(Category)
# admin.site.register(Professor)
# admin.site.register(Student)


@admin.register(Professor)
class ProfesorAdmin(admin.ModelAdmin):
    fields = ["username", "email", "first_name", "category", "title", "numero_trabajador"]



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ["username", "email", "first_name", "matricula"]

