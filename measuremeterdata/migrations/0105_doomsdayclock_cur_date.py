# Generated by Django 3.0.5 on 2021-07-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0104_auto_20210423_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='doomsdayclock',
            name='cur_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
