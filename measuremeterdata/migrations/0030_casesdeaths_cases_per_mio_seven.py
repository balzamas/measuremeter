# Generated by Django 3.0.5 on 2020-06-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0029_auto_20200531_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='casesdeaths',
            name='cases_per_mio_seven',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]