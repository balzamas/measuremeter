# Generated by Django 3.0.5 on 2020-10-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0056_belprovince_hasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casesdeaths',
            name='deathstotal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]