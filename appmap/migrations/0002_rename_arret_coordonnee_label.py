# Generated by Django 5.0.1 on 2024-01-29 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordonnee',
            old_name='arret',
            new_name='label',
        ),
    ]
