# Generated by Django 3.0.5 on 2020-05-13 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0019_country_isactive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measure',
            name='none',
        ),
        migrations.RemoveField(
            model_name='measure',
            name='partial',
        ),
    ]
