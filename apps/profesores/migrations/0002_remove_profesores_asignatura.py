# Generated by Django 5.1.2 on 2024-10-25 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesores',
            name='asignatura',
        ),
    ]