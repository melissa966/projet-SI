# Generated by Django 4.0 on 2022-01-17 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_stage_id_alter_stage_codestage'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='TypeStage',
            field=models.CharField(default='1CS', max_length=10),
        ),
    ]
