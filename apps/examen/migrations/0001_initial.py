# Generated by Django 5.1.2 on 2024-10-25 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumnos', '0001_initial'),
        ('asignaturas', '0001_initial'),
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField()),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignaturas.asignaturas')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesores.profesores')),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionExamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField()),
                ('observacion', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('fecha_creacion', models.DateField()),
                ('fecha_resolucion', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumnos')),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examen.examen')),
            ],
        ),
    ]
