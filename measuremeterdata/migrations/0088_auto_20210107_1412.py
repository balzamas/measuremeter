# Generated by Django 3.0.5 on 2021-01-07 13:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0087_auto_20210107_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrymeasure',
            name='comment',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
