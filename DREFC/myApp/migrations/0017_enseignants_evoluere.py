# Generated by Django 4.0 on 2022-01-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0016_stagiaire_type_de_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignants',
            name='EvoluerE',
            field=models.ManyToManyField(related_name='evoluerpar', to='myApp.Stage'),
        ),
    ]
