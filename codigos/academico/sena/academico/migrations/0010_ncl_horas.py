# Generated by Django 4.0 on 2022-11-30 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0009_alter_ncl_cod'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncl',
            name='horas',
            field=models.CharField(default=0, max_length=5),
        ),
    ]
