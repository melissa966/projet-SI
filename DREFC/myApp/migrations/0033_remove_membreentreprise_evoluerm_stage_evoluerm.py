# Generated by Django 4.0 on 2022-01-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0032_entreprise_evoluere'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membreentreprise',
            name='EvoluerM',
        ),
        migrations.AddField(
            model_name='stage',
            name='EvoluerM',
            field=models.ManyToManyField(related_name='evoluerpar', to='myApp.MembreEntreprise'),
        ),
    ]
