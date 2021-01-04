# Generated by Django 3.0.5 on 2021-01-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0081_oxfordmeasure_last_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='casesdeaths',
            name='stringency_index',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='chcases',
            name='kof_index',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True),
        ),
    ]
