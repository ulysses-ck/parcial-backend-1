# Generated by Django 5.1.2 on 2024-10-25 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='asignatura',
        ),
    ]
