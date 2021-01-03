# Generated by Django 3.0.5 on 2021-01-03 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0077_casesdeaths_deaths_past7days'),
    ]

    operations = [
        migrations.CreateModel(
            name='OxfordMeasureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=2)),
                ('text_level0', models.CharField(max_length=200)),
                ('text_level1', models.CharField(max_length=200)),
                ('text_level2', models.CharField(max_length=200)),
                ('text_level3', models.CharField(max_length=200)),
                ('text_level4', models.CharField(max_length=200)),
                ('isactive', models.BooleanField(default=True)),
                ('icon', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OxfordMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('level', models.IntegerField(default=0)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measuremeterdata.Country')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measuremeterdata.OxfordMeasureType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]