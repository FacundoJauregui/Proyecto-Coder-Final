# Generated by Django 4.0.4 on 2022-06-28 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(choices=[('MAN', 'Manga')], max_length=5)),
                ('volumenes', models.IntegerField()),
                ('published', models.DateField()),
                ('status', models.CharField(choices=[('FIN', 'Finished'), ('PUB', 'Publishing')], max_length=10)),
                ('genres', models.CharField(max_length=70)),
                ('author', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Studios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('fundation_date', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(default='Bienvenido', max_length=120)),
                ('image', models.ImageField(default='default.png', upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(choices=[('MOV', 'Movie'), ('TV', 'Tv'), ('ONA', 'Ona'), ('OVA', 'Ova')], max_length=5)),
                ('episodes', models.IntegerField()),
                ('relase_date', models.DateField()),
                ('genres', models.CharField(max_length=70)),
                ('duration', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('backgroun', models.TextField(default='Sin Antecedentes')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studio', to='ProyectoFinal.studios')),
            ],
        ),
    ]