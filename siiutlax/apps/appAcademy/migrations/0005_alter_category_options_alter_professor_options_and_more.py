<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-06-29 04:27
=======
# Generated by Django 5.0.6 on 2024-07-04 19:22
>>>>>>> origin

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAcademy', '0004_rename_students_student_delete_principal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.AlterField(
            model_name='professor',
            name='numero_trabajador',
            field=models.IntegerField(),
        ),
    ]
