# Generated by Django 4.0 on 2022-01-23 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0041_remove_stage_etudiant_stagiaiare_stage_grp_etd'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='entreprise',
            field=models.ForeignKey(blank=True, null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, to='myApp.entreprise'),
            preserve_default=b'I01\n',
        ),
    ]
