# Generated by Django 4.0 on 2022-01-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0030_remove_evoluem_membre_entreprise_jury_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membreentreprise',
            name='EvoluerM',
            field=models.ManyToManyField(related_name='evoluerpar', to='myApp.Stage'),
        ),
    ]
