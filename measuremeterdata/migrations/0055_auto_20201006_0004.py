# Generated by Django 3.0.5 on 2020-10-05 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0054_belagegroups_belcases_belprovince'),
    ]

    operations = [
        migrations.AlterField(
            model_name='belprovince',
            name='name_source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
