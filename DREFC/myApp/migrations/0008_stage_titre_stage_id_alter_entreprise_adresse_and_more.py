# Generated by Django 4.0 on 2022-01-19 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_remove_entreprise_id_entreprise_adresse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='Titre',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='stage',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='adresse',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='stage',
            name='codeStage',
            field=models.CharField(default='', max_length=10),
        ),
    ]