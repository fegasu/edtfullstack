# Generated by Django 4.0 on 2022-11-30 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AREAS',
            new_name='AREA',
        ),
        migrations.RenameModel(
            old_name='FICHAS',
            new_name='FICHA',
        ),
    ]
