# Generated by Django 4.0 on 2022-01-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0039_rename_mail_enseignants_mail_ens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='EvoluerM',
            field=models.ManyToManyField(related_name='evoluer', to='myApp.MembreEntreprise'),
        ),
    ]
