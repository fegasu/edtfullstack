# Generated by Django 4.0 on 2022-11-30 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0003_alter_actividad_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='estado',
            field=models.IntegerField(choices=[(1, 'ACTIVO'), (2, 'INACTIVO')], default=1),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='estado',
            field=models.IntegerField(choices=[(1, 'ACTIVO'), (2, 'INACTIVO')], default=1),
        ),
    ]
