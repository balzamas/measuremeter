# Generated by Django 3.0.5 on 2021-04-21 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0100_auto_20210421_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doomsdayclock',
            old_name='positivity_value',
            new_name='positivity_7d',
        ),
        migrations.RemoveField(
            model_name='doomsdayclock',
            name='positivity_value_7d',
        ),
    ]