# Generated by Django 3.0.5 on 2020-12-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0074_auto_20201219_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='casesdeaths',
            name='deathstotal_average',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True),
        ),
    ]
