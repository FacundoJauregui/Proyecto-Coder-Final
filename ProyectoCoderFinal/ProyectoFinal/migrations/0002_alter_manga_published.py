# Generated by Django 4.0.4 on 2022-06-28 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoFinal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='published',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
    ]
