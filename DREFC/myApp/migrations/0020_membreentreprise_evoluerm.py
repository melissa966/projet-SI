# Generated by Django 4.0 on 2022-01-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_remove_membreentreprise_type_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='membreentreprise',
            name='EvoluerM',
            field=models.ManyToManyField(related_name='evoluerPar', to='myApp.Stage'),
        ),
    ]
