# Generated by Django 3.0.5 on 2020-11-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0062_auto_20201105_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casesdeaths',
            name='cases_per_mio',
        ),
        migrations.RemoveField(
            model_name='casesdeaths',
            name='cases_per_mio_seven',
        ),
        migrations.RemoveField(
            model_name='casesdeaths',
            name='deaths_per100k',
        ),
        migrations.RemoveField(
            model_name='casesdeaths',
            name='deaths_total_per100k',
        ),
        migrations.AddField(
            model_name='country',
            name='peak_year',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
