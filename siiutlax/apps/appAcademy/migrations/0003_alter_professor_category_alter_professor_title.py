# Generated by Django 5.0.6 on 2024-06-28 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAcademy', '0002_category_professor_title_alter_students_matricula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appAcademy.category'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
