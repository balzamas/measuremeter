# Generated by Django 3.0.5 on 2020-09-15 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0048_auto_20200915_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='mapcode_europe',
        ),
    ]