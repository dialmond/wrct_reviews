# Generated by Django 5.0.1 on 2024-08-20 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='status',
            field=models.CharField(blank=True, choices=[('Bin', 'Bin'), ('N&WC', 'New and Way Cool'), ('NIB', 'Never in bin'), ('TBR', 'To be reviewed'), ('OOB', 'Out of bin'), ('Missing', 'Missing'), ('Library', 'Library')], max_length=7, null=True),
        ),
    ]
