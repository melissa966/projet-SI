# Generated by Django 4.0 on 2022-01-19 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_stage_titre_stage_id_alter_entreprise_adresse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignatns',
            fields=[
                ('IDens', models.BigAutoField(primary_key=True, serialize=False)),
                ('NomE', models.CharField(max_length=20)),
                ('PrenomE', models.CharField(max_length=20)),
                ('Grade', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MembreEntreprise',
            fields=[
                ('Id_m', models.IntegerField(primary_key=True, serialize=False)),
                ('Fonction', models.CharField(max_length=50)),
                ('NomM', models.CharField(max_length=50)),
                ('PrenomM', models.CharField(max_length=50)),
                ('Mail', models.CharField(max_length=25)),
            ],
        ),
        migrations.RenameField(
            model_name='entreprise',
            old_name='idEntreprise',
            new_name='IdEnt',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='raisonSociale',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='codeStage',
        ),
        migrations.AddField(
            model_name='entreprise',
            name='Adresse',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entreprise',
            name='NomEntreprise',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='Secteur',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stage',
            name='DateDeb',
            field=models.DateField(default='2015-01-19'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stage',
            name='DateDepot',
            field=models.DateField(default='2015-01-19'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stage',
            name='Note',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stage',
            name='Titre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='stage',
            name='TypeStage',
            field=models.CharField(max_length=4),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='membre2',
            field=models.ForeignKey(blank=True, null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, to='myApp.membreentreprise'),
            preserve_default=b'I01\n',
        ),
        migrations.AddField(
            model_name='stage',
            name='membre',
            field=models.ForeignKey(blank=True, null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, to='myApp.membreentreprise'),
            preserve_default=b'I01\n',
        ),
    ]
