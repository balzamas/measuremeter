# Generated by Django 3.0.5 on 2021-02-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0092_doomsdayclock_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='doomsdayclock',
            name='r_okay',
            field=models.BooleanField(default=False),
        ),
    ]