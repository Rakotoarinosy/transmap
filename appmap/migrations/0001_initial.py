# Generated by Django 5.0.1 on 2024-01-25 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Coordonnee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='chemin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appmap.bus', verbose_name='relation bus')),
                ('idCor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appmap.coordonnee', verbose_name='relation coordonnee')),
            ],
        ),
    ]