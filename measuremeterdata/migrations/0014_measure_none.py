# Generated by Django 3.0.5 on 2020-05-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0013_auto_20200501_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='measure',
            name='none',
            field=models.BooleanField(default=False),
        ),
    ]