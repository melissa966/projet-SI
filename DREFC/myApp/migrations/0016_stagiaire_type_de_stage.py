# Generated by Django 4.0 on 2022-01-21 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0015_rename_ecole_enseignants_université'),
    ]

    operations = [
        migrations.AddField(
            model_name='stagiaire',
            name='Type_de_stage',
            field=models.ForeignKey(blank=True, null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, to='myApp.stage'),
            preserve_default=b'I01\n',
        ),
    ]
