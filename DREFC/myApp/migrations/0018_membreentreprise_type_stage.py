# Generated by Django 4.0 on 2022-01-21 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_enseignants_evoluere'),
    ]

    operations = [
        migrations.AddField(
            model_name='membreentreprise',
            name='type_stage',
            field=models.ForeignKey(blank=True, null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, to='myApp.stage'),
            preserve_default=b'I01\n',
        ),
    ]
