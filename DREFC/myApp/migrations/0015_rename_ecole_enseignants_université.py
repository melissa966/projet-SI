# Generated by Django 4.0 on 2022-01-21 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_enseignants_ecole'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enseignants',
            old_name='Ecole',
            new_name='Universit√©',
        ),
    ]
